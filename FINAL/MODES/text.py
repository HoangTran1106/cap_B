from flask import stream_with_context
import cv2
from ultralytics import YOLO
import keyboard
import time
import json
from threading import Lock
# import time
# import io
# import base64
# import json
# from threading import Lock

def toggle_allow_Text_Mode():
	global allow_Text_Mode
	allow_Text_Mode = not allow_Text_Mode
	print(f'\n\nallow_Text_Mode is now: {allow_Text_Mode}\n\n')

def toggle_pause():
	global pause
	pause = not pause
	print(f'\n\npause is now: {pause}\n\n')

def generate_Text_Lock(global_vars):
	# Shared counter and lock for thread safety
	global active_connections
	active_connections = 0
	counter_lock = Lock()
	@stream_with_context
	def generate_Text ():
		global active_connections
		with counter_lock:
			active_connections += 1
			print(f"Active connections: {active_connections}")
		try:
			while True:	
				camera = global_vars['camera']
				#camera = cv2.VideoCapture(0)
				model = global_vars['model']
				allow_Text_Mode = global_vars['allow_Text_Mode']
				pause = global_vars['Text_pause']
				prev_data = global_vars['Text_prev_data'] 
				conf_threshold = global_vars['conf_threshold']
				if not allow_Text_Mode:
					data = {'message': 'Text_Mode_stopped'}
					global_vars['detect_info'] = data
					yield(f"data: {json.dumps(data)}\n\n")
					return
				success, frame = camera.read()
				# print("\nCamera Open: " + str(success))
				if not success:
					return {'message': "Fail to open camera !!"}
				if pause:
					data = {'message': prev_data}
					global_vars['detect_info'] = data
					yield(f"data: {json.dumps(data)}\n\n")
					time.sleep(1)
					continue
				results = model(frame)
				fire_list = []
				smoke_list = []
				for box in results[0]:
					# Get the confidence score
					box_ = box.boxes
					print(box_.conf.item())
					print(type(box_.conf.item()))
					#print(model.names[int(cls)])
					cls = box_.cls.item()
					print(model.names[int(cls)])
					if box_.conf.item() < conf_threshold:
						continue
					if model.names[int(cls)].lower() == "fire":
						fire_list.append(box_.conf.item())
					elif model.names[int(cls)].lower() == "smoke":
						smoke_list.append(box_.conf.item())
				fire_list = [str(round(fire, 2)) for fire in fire_list]
				smoke_list = [str(round(smoke, 2)) for smoke in smoke_list]
				prev_data = {
					"fire":fire_list,
					"smoke":smoke_list
				}
				print(prev_data)
				data = {'message': prev_data}
				global_vars['detect_info'] = data
				yield(f"data: {json.dumps(data)}\n\n")
				time.sleep(1)
		except GeneratorExit:
			# This block is triggered when the client disconnects
			print("Client disconnected from stream.")
		except Exception as e:
			print(e)
		finally:
			# Decrement active connections
			with counter_lock:
				active_connections -= 1
				print (active_connections)
	return generate_Text()

if __name__ == "__main__":
	camera = cv2.VideoCapture(0)
	# model = YOLO('m_100k_250epoch.engine')
	model = YOLO('../best_120.pt')
	conf_threshold = 0.2
	# Control Var
	allow_Text_Mode = True
	Text_pause = False
	# DATA sent 
	Text_prev_data = ""

	# keyboard.on_press_key("k", lambda _: toggle_allow_Text_Mode())
	# keyboard.on_press_key("p", lambda _: toggle_pause())
	### 
	while(True): 
		if allow_Text_Mode:
			output = generate_Text_Lock(globals())
			print(next(output))
			print(detect_info_1)
		else:
			break
