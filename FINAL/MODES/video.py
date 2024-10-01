import imageio_ffmpeg as ffmpeg
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
			class_name = model.names[int(cls)].lower()
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
			allow_Video_Mode = global_vars['allow_Video_Mode']
			output_file = global_vars['output_file']
			File_Export_BOOL = global_vars['File_Export_BOOL']
			camera = global_vars['camera']
			if not camera.isOpened():
				camera = cv2.VideoCapture(0)
			vid_len = 30
			frame_width = 640
			frame_height = 480
			#fps = 10
			skip_frames = 1
			sys_info = "plhold"
			#start_time = time.time()
			output_params = [
				'-vcodec', 'libx264',  # Use H.264 codec
				'-crf', '23',  # Constant Rate Factor (lower is better quality, but larger file)
				'-preset', 'medium',  # Encoding speed (slower is better compression)
				'-pix_fmt', 'yuv420p'  # Pixel format (yuv420p is widely compatible)
			]
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
			#if not File_Export_BOOL:
				#return {"message": "please enable file export"}
			#fourcc = cv2.VideoWriter_fourcc(*'mp4v')
			#out = cv2.VideoWriter('output_file.mp4', fourcc, 30.0, (640, 480))
			# Set the start time
			out = ffmpeg.write_frames('./output.mp4', (frame_width, frame_height), fps=30, output_params=output_params)
			out.send(None)  # Initialize the out
			start_time = time.time()
			if not allow_Video_Mode:
				return {"message": "please turn Video Mode on !!"}
			# Record for 5 seconds
			while(True):
				print(start_time, time.time())
				cond_ = (int(time.time()) - int(start_time)) > vid_len
				timestamp = (int(time.time()) - int(start_time))*1000
				print(timestamp)
				ret, frame = camera.read()
				#print(ret)
				#if skip_frames == 50:
					#frame, sys_info = process_frame(frame, global_vars)
					#skip_frames -= 1
				if ret==True:
					#start_time = time.time()
					# Write the frame
					#start_time = time.time()
					frame, sys_info = process_frame(frame, global_vars)
					#
					frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				        # Write th
					out.send(frame_rgb)
					#out = ffmpeg.write_frames('output_file.mp4', (frame_width, frame_height), fps=30, output_params=output_params)
		                        #out.send(None)  # Initialize the out
					#out.write(frame)
					#timestamp = int((time.time() - start_time) * 1000)  # milliseconds
					#out.set(cv2.CAP_PROP_POS_MSEC, timestamp)
				else:
					break
			    	# Check if 5 seconds have passed
				if cond_:
					print(start_time, cond_)
					camera.release()
					out.close()
					#camera = cv2.VideoCapture(0)
					return(sys_info)

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
	output_file = '../output.webm'

	# keyboard.on_press_key("k", lambda _: toggle_allow_Video_Mode())
	# keyboard.on_press_key("p", lambda _: toggle_pause())
	###
	if allow_Video_Mode:
		generate_Video_Lock(globals())
		#print(detect_info_3)

