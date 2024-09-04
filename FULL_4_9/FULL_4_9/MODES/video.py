from flask import stream_with_context
import cv2
from ultralytics import YOLO
import keyboard
import time
# import io
# import base64
# import json
from threading import Lock

def toggle_allow_Video_Mode():
	global allow_Video_Mode
	allow_Video_Mode = not allow_Video_Mode
	print(f'\n\nallow_Video_Mode is now: {allow_Video_Mode}\n\n')

def toggle_pause():
	global pause
	pause = not pause
	print(f'\n\npause is now: {pause}\n\n')

def detect_objects(frame, global_vars):
	model = global_vars['model'] 
	conf_threshold = global_vars['conf_threshold']
	
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
		cls = box['class']
		conf = box['confidence']
		if conf < conf_threshold:
			continue
		if cls == "fire":
			fire_list.append(conf)
		elif cls == "smoke":
			smoke_list.append(conf)

	fire_list = [str(round(fire, 2)) for fire in fire_list]
	smoke_list = [str(round(smoke, 2)) for smoke in smoke_list]
	prev_data = {
		"fire":fire_list,
		"smoke":smoke_list
	}
	sys_info = {'message': prev_data}

	cv2.putText(frame, f"Confidence threshold: {conf_threshold:.2f}", (10, 60),
				cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

	return frame, sys_info


def generate_Video_Lock(global_vars):
	global active_connections
	active_connections = 0
	counter_lock = Lock()

	def generate_Video (global_vars):
		global active_connections
		with counter_lock:
			active_connections += 1
		try:
			#time.sleep(0.3)
			global sys_info
			output_file = global_vars['output_file']
			camera = global_vars['camera']
			vid_len = 5
			frame_width = 640
			frame_height = 480
			fps = 10
			start_time = time.time()
			"""
			fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for webm
			out_mp4 = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))    
			while int(time.time() - start_time) < vid_len:
				success, frame = camera.read()
				print(time.time() - start_time)
				if not success:
					return {'message': "Fail to open camera !!"}
				frame, sys_info = process_frame(frame, global_vars)
				out_mp4.write(frame)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break
			camera.release()
			out_mp4.release()
			"""
			fourcc = cv2.VideoWriter_fourcc(*'XVID')
			out = cv2.VideoWriter('output_file.avi', fourcc, 20.0, (640, 480))

			# Set the start time
			start_time = time.time()

			# Record for 5 seconds
			while(camera.isOpened()):
			    ret, frame = camera.read()
			    if ret==True:
			        # Write the frame
			        frame, sys_info = process_frame(frame, global_vars)
			        out.write(frame)
			    else:
			        break
			    
			    # Check if 5 seconds have passed
			    if time.time() - start_time > 5:
			        camera.release()
			        out.release()
			        break

			# Release everything when done
		except GeneratorExit:
			# This block is triggered when the client disconnects
			print("Client disconnected from stream.")
		except Exception as e:
			raise Exception(f"Error during video capture: {str(e)}")
		finally:
			# Decrement active connections
			with counter_lock:
				active_connections -= 1
		return sys_info
	return generate_Video(global_vars)

if __name__ == "__main__":
	camera = cv2.VideoCapture(0)
	model = YOLO('../best_120.pt')
	conf_threshold = 0.2
	# Control Var
	allow_Video_Mode = True
	pause = False
	# Video Configuration
	vid_len = 3
	frame_width = 640
	frame_height = 480
	fps = 30
	output_file = '../output.mp4'

	# keyboard.on_press_key("k", lambda _: toggle_allow_Video_Mode())
	# keyboard.on_press_key("p", lambda _: toggle_pause())
	### 
	if allow_Video_Mode:
		output = generate_Video_Lock(globals())
		print(detect_info_3)

