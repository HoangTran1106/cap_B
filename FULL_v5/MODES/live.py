from flask import stream_with_context
from ultralytics import YOLO
import cv2
import numpy as np
import time
from threading import Lock
from collections import defaultdict

def generate_Live_Lock (globals_var):
	global active_connections, detect_info_4
	active_connections = 0
	counter_lock = Lock()
	# @stream_with_context
	def generate_Live(globals_var):
		allow_Live_Mode = globals_var['allow_Live_Mode']
		detection_active = globals_var['detection_active']
		conf_threshold = globals_var['conf_threshold']
		Live_Mode_Live_Only_control = globals_var['Live_Mode_Live_Only_control']
		SIZE_output = globals_var['SIZE_output']
		camera = globals_var['camera']
		model = globals_var['model']
		track_history = globals_var['track_history']
		global active_connections, detect_info_4
		with counter_lock:
			active_connections += 1
			# print(f"Active connections: {active_connections}")
		try:
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
						
				# detection_active = globals_var['detection_active']
				allow_Live_Mode = globals_var['allow_Live_Mode']
				detection_active = globals_var['detection_active']
				conf_threshold = globals_var['conf_threshold']
				Live_Mode_Live_Only_control = globals_var['Live_Mode_Live_Only_control']
				SIZE_output = globals_var['SIZE_output']
				camera = globals_var['camera']
				model = globals_var['model']
				track_history = globals_var['track_history']
				if detection_active:
					prev_time = time.time()
					results = model.track(frame, persist=True, conf=conf_threshold)
					inference_time = time.time() - prev_time
					# #
					# print("Type of results[0].boxes:", type(results[0].boxes))
					# print("Shape of results[0].boxes:", getattr(results[0].boxes, 'shape', 'No shape attribute'))			
					fire_list = []
					smoke_list = []
					for box in results[0].boxes:
						cls = box.cls.cpu()[0].numpy()
						cls = int(cls)
						conf = box.conf.cpu()[0].numpy()
						conf = float(conf)
						print(conf, cls)
						if conf < conf_threshold:
							continue
						if cls == 0:
							fire_list.append(conf)
						elif cls == 1:
							smoke_list.append(conf)

					fire_list = [str(round(fire, 2)) for fire in fire_list]
					smoke_list = [str(round(smoke, 2)) for smoke in smoke_list]
					data = "Fire - " + str(len(fire_list)) + ": " + ", ".join(fire_list) \
									+ "\nSmoke - " + str(len(smoke_list)) + ": " + ", ".join(smoke_list)
					print(data)
					data = {'message': data}
					detect_info_4 = data
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
		except GeneratorExit:
			# This block is triggered when the client disconnects
			print("Client disconnected from stream.")
		finally:
			# Decrement active connections
			with counter_lock:
				active_connections -= 1

		if not Live_Mode_Live_Only_control:
			camera.release()
			cv2.destroyAllWindows()
	return generate_Live(globals_var)

if __name__ == '__main__':
	allow_Live_Mode = True
	detection_active = True
	conf_threshold = 0
	Live_Mode_Live_Only_control = True
	SIZE_output = (928,480)
	camera = cv2.VideoCapture(0)
	model = YOLO('../best_120.pt')
	track_history = defaultdict(lambda: [])
	detect_info_4 = ""

	while True:
		# Assume 'byte_data' is the series of bytes representing the image.
		byte_data = next(generate_Live_Lock(globals())) # Replace with your byte data

		# Find the position of the header end (the position of '\r\n\r\n')
		header_end = byte_data.find(b'\r\n\r\n') + 4

		# Extract the actual JPEG frame data by skipping the header
		jpeg_frame_data = byte_data[header_end:]

		# Convert the JPEG byte data back to a NumPy array
		nparr = np.frombuffer(jpeg_frame_data, np.uint8)

		# Decode the bytes into an image
		decoded_frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

		# Check if the frame was successfully decoded
		if decoded_frame is None:
			print("Error: Unable to decode image")
		else:
			# Display the decoded frame
			cv2.imshow("Decoded Frame", decoded_frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		print(detect_info_4)
	cv2.waitKey(0)  # Wait for a key press to close the window
	cv2.destroyAllWindows()