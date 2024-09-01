from flask import Flask, render_template, Response, jsonify, request
from ultralytics import YOLO
import cv2
import numpy as np
import time

from collections import defaultdict

app = Flask(__name__)

# Global variables
# camera = cv2.VideoCapture("/dev/video0")
camera = cv2.VideoCapture(0)
# model = YOLO('m_100k_250epoch.engine')
model = YOLO('m_100k_250epoch.pt')
conf_threshold = 0.5
SIZE_output = (928,480)

detection_active = False
allow_Live_Mode = False
allow_Video_Mode = False
allow_Capture_Mode = False
allow_Text_Mode = False

Live_Mode_Live_Only_control = False
track_history = defaultdict(lambda: [])

def generate_frames():
	global detection_active, conf_threshold, inference_time
	while not allow_Live_Mode:
		try:
			yield(prev_img)
		except:
			_image = cv2.imread('./plchold.jpg')
			_image = cv2.resize(_image, SIZE_output)
			success, encoded_image = cv2.imencode('.jpg', _image)
			image_bytes = encoded_image.tobytes()
			yield((b'--frame\r\n'
			   b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n'))
	fps = 0
	while True:
		prev_time = time.time()
		success, frame = camera.read()
		#print(success)
		if not success:
			break
		inference_time = time.time() - prev_time

		# Create a wider frame with space on the right
		height, width = frame.shape[:2]
		wide_frame = np.zeros((height, int(width * 1.45), 3), dtype=np.uint8)
		wide_frame[:, :width] = frame                

		if detection_active:
			prev_time = time.time()
			results = model.track(frame, persist=True, conf=conf_threshold)
			inference_time = time.time() - prev_time
			# print(results)
			# print(results, results[0].boxes, results[0].boxes.id)
			if len(results[0].boxes) == 0 or results[0].boxes.id == None:
				pass
			else:
				boxes = results[0].boxes.xywh.cpu()
				track_ids = results[0].boxes.id.int().cpu().tolist()

				# Visualize the results on the frame
				annotated_frame = results[0].plot()

				# Plot the tracks
				for box, track_id in zip(boxes, track_ids):
					x, y, w, h = box
					track = track_history[track_id]
					track.append((float(x), float(y)))  # x, y center point
					if len(track) > 30:  # retain 90 tracks for 90 frames
						track.pop(0)

					# Draw the tracking lines
					points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
					cv2.polylines(annotated_frame, [points], isClosed=False, color=(230, 230, 230), thickness=10)
				wide_frame[:, :width] = annotated_frame                

		# Add FPS, inference time, and confidence threshold to the right side
		fps = 1/inference_time
		inference_time = inference_time*1000
		cv2.putText(wide_frame, f'FPS: {fps:.2f}', (width + 10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
		cv2.putText(wide_frame, f'Inference: {inference_time:.2f}ms', (width + 10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
		cv2.putText(wide_frame, f'Conf Threshold: {conf_threshold:.2f}', (width + 10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
		
		# Encode the frame as JPEG
		_, buffer = cv2.imencode('.jpg', wide_frame)
		frame = buffer.tobytes()
		prev_img = (b'--frame\r\n'
			   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
		yield prev_img
		if cv2.waitKey(1) == ord('q'):
			break
	if Live_Mode_Live_Only_control:
		camera.release()
		cv2.destroyAllWindows()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/video_feed')
def video_feed():
	return Response(generate_frames(),
					mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_detection')
def start_detection():
	global detection_active
	detection_active = True
	return jsonify({"status": "started"})

@app.route('/stop_detection')
def stop_detection():
	global detection_active
	detection_active = False
	return jsonify({"status": "stopped"})

@app.route('/set_threshold', methods=['POST'])
def set_threshold():
	global conf_threshold, detection_active
	data = request.get_json()
	if not detection_active:
		conf_threshold = float(data['threshold'])
		return jsonify({"status": "threshold updated", "new_threshold": conf_threshold})
	else:
		return jsonify({"status": "error", "message": "Cannot change threshold during detection"})

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=False)
