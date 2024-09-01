from flask import stream_with_context
import cv2
from ultralytics import YOLO
import keyboard
# import time
# import io
# import base64
# import json
from threading import Lock

def toggle_allow_Capture_Mode():
	global allow_Capture_Mode
	allow_Capture_Mode = not allow_Capture_Mode
	print(f'\n\nallow_Capture_Mode is now: {allow_Capture_Mode}\n\n')

def toggle_pause():
	global pause
	pause = not pause
	print(f'\n\npause is now: {pause}\n\n')

def detect_objects(frame, global_vars):
	conf_threshold = global_vars['conf_threshold']
	model = global_vars['model']
	results = model(frame)

	detections = []
	for r in results:
		boxes = r.boxes
		for box in boxes:
			b = box.xyxy[0].tolist()
			conf = box.conf.item()
			cls = box.cls.item()
			class_name = model.names[int(cls)]
			if class_name in ['fire', 'smoke'] and conf >= conf_threshold:
				detections.append({
					'class': class_name,
					'confidence': conf,
					'bbox': b
				})
	return detections

def process_frame(frame, global_vars):
	global detect_info_2
	conf_threshold = global_vars['conf_threshold']
	detections = detect_objects(frame, global_vars)

	# Draw bounding boxes on the frame
	for det in detections:
		bbox = det['bbox']
		cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 255, 0), 2)
		cv2.putText(frame, f"{det['class']} {det['confidence']:.2f}", (int(bbox[0]), int(bbox[1])-10),
					cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
	
	fire_list = []
	smoke_list = []
	for box in detections:
		# Get the confidence score
		box = box['class']
		conf = box['confidence']
		if conf < conf_threshold:
			continue
		if box == "fire":
			fire_list.append(conf)
		elif box == "smoke":
			smoke_list.append(conf)

	fire_list = [str(round(fire, 2)) for fire in fire_list]
	smoke_list = [str(round(smoke, 2)) for smoke in smoke_list]
	prev_data = "Fire - " + str(len(fire_list)) + ": " + ", ".join(fire_list) \
					+ "\nSmoke - " + str(len(smoke_list)) + ": " + ", ".join(smoke_list)
	print(prev_data)
	data = {'message': prev_data}
	detect_info_2 = data

	cv2.putText(frame, f"Confidence threshold: {conf_threshold:.2f}", (10, 60),
				cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

	return frame


def generate_Capture_Lock(global_vars):
# Shared counter and lock for thread safety
	global active_connections
	active_connections = 0
	counter_lock = Lock()
	@stream_with_context
	def generate_Capture():
		prev_data = global_vars['Capture_prev_data']
		global active_connections
		with counter_lock:
			active_connections += 1
			print(f"Active connections: {active_connections}")
		try:
			camera = global_vars['camera']
			success, frame = camera.read()
			if not success:
				return {'message': 'Fail to open camera!!'}
			prev_data = process_frame(frame, global_vars)
			cv2.imwrite('../output_capture.png', prev_data)
		except GeneratorExit:
			# This block is triggered when the client disconnects
			print("Client disconnected from stream.")
		finally:
			# Decrement active connections
			with counter_lock:
				active_connections -= 1
		# print(f"Active connections: {active_connections}")
	return generate_Capture()

if __name__ == "__main__":
	camera = cv2.VideoCapture(0)
	# model = YOLO('m_100k_250epoch.engine')
	model = YOLO('../best_120.pt')
	conf_threshold = 0.2
	# Control Var
	allow_Capture_Mode = True
	pause = True
	# DATA sent
	_image = cv2.imread('../plchold.jpg')
	Capture_prev_data = _image

	# keyboard.on_press_key("k", lambda _: toggle_allow_Capture_Mode())
	# keyboard.on_press_key("p", lambda _: toggle_pause())
	### 
	if allow_Capture_Mode:
		output = generate_Capture_Lock(globals())
		print(detect_info_2)
		cv2.waitKey(1)
