from flask import Flask, render_template, Response, jsonify, request, send_file, abort
import os 
from flask_cors import CORS
from ultralytics import YOLO
import cv2
import numpy as np
import time
from MODES.text import generate_Text_Lock 
from MODES.capture import generate_Capture_Lock 
from MODES.video import generate_Video_Lock 
from MODES.live import generate_Live_Lock
import json
import sys_info

from collections import defaultdict

app = Flask(__name__)
CORS(app)

# Global variables
# camera = cv2.VideoCapture("/dev/video0")
# model = YOLO('best_new_5.engine')

# For development
camera = cv2.VideoCapture(0)
model = YOLO('best_120.pt')

conf_threshold = 0.5
SIZE_output = (928,480)

allow_Live_Mode = False
allow_Video_Mode = False
allow_Capture_Mode = False
allow_Text_Mode = False

## Info route 
"""
values of detect_info:
Luc bat dau. "" 
## Text Mode
{'message': "Fail to open camera !!"}
{'message': 'Text_Mode_stopped'}
## Capture Mode
{'message': 'Fail to open camera !!'}
## Video Mode
{'message': "Fail to open camera !!"}
## Live Mode
{'message': 'Live mode started !!'}
### Con lai
detect_info = {
	'fire': fire_list,
	'smoke':smoke_list
}
"""
detect_info = ""


## Text Mode
Text_pause = True
Text_prev_data = "No detection"
## Capture Mode
Capture_prev_data = cv2.imread('./plchold.jpg')
_, buffer = cv2.imencode('.jpg', Capture_prev_data)
Capture_prev_data = buffer.tobytes()
Capture_prev_data = (b'--frame\r\n'
		b'Content-Type: image/jpeg\r\n\r\n' + Capture_prev_data + b'\r\n')
Capture_get = False
## Video Mode
output_file = './output_video.webm'
File_Export_BOOL = False
## Live Mode
Live_Mode_Live_Only_control = False
detection_active = False
track_history = defaultdict(lambda: [])

def modeOn_Off (mode_turned):
	lis_t  = ['allow_Text_Mode', 'allow_Capture_Mode', 'allow_Video_Mode', 'allow_Live_Mode']
	globals()[lis_t[mode_turned - 1]] = True 
	for x_ in lis_t:
		if x_ != lis_t[mode_turned - 1]:
			globals()[x_] = False

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/info')
def info():
	global detect_info
	lis_t  = ['allow_Text_Mode', 'allow_Capture_Mode', 'allow_Video_Mode', 'allow_Live_Mode']
	info_ = sys_info.log_gps_and_network_data()
	return jsonify({
		'fire_n_smoke':	detect_info,
		'info': info_
	})

@app.route('/mode_Control', methods=['POST'])
def mode_Control ():
	global allow_Live_Mode, allow_Capture_Mode, allow_Video_Mode, allow_Text_Mode
	#
	try:
		data = request.get_json()
		mode_change = data['mode_turned']
		modeOn_Off(mode_change)
	except:
		lis_t  = ['allow_Text_Mode', 'allow_Capture_Mode', 'allow_Video_Mode', 'allow_Live_Mode']
		print("Not receive ")
		for x_ in lis_t:
			globals()[x_] = False
	return jsonify({"mode_Control": {
		# 'detection_active' : detection_active,
		'allow_Live_Mode' : globals()['allow_Live_Mode'],
		'allow_Video_Mode' : globals()['allow_Video_Mode'],
		'allow_Capture_Mode' : globals()['allow_Capture_Mode'],
		'allow_Text_Mode' : globals()['allow_Text_Mode'],
	}})

########################## Text Mode
@app.route('/TextMode/feed')
def TextMode_feed ():
	global detect_info
	# if not allow_Text_Mode:
	# 	return Response(json.dumps('TextMode_disabled'), mimetype='text/event-stream')
	ret_val = generate_Text_Lock(globals())
	detect_info = ret_val
	ret_val = f"data: {json.dumps(ret_val)}\n\n"
	return Response(ret_val,
				 mimetype='text/event-stream')


@app.route('/TextMode/control', methods=['POST'])
def TextMode_control ():
	global allow_Text_Mode, Text_pause
	data = request.get_json()
	# allow_Text_Mode = data['allow_Text_Mode']
	Text_pause = data['Text_pause']
	return jsonify({
		'status': 'TextMode_control_success',
		# 'allow_Text_Mode': allow_Text_Mode,
		'Text_pause': Text_pause
	})

########################## Capture Mode
@app.route('/CaptureMode/feed') 
def CaptureMode_feed():
	global detect_info
	# Path to the image file
	file_path = './output_capture.png'
	_check = generate_Capture_Lock(globals())
	if _check != None and _check['message'] == 'Fail to open camera !!':
		abort(404, description="Fail to open camera !!")
	else:
		detect_info = _check

	# Check if the file exists
	if not os.path.exists(file_path):
		# Return a 404 Not Found error if the file does not exist
		abort(404, description="File not found")

	# Send the file if it exists
	return send_file(file_path, mimetype='image/png')

@app.route('/CaptureMode/control', methods=['POST'])
def CaptureMode_control ():
	global allow_Capture_Mode, Capture_get
	data = request.get_json()
	# allow_Capture_Mode = data['allow_Capture_Mode']
	Capture_get = data['Capture_get']
	# print(allow_Capture_Mode)
	return jsonify({
		'status': 'CaptureMode_control_success',
		# 'allow_Capture_Mode': allow_Capture_Mode,
		'Capture_get': Capture_get
	})

########################## Video Mode
@app.route('/VideoMode/getVideo')
def send_Video():
	global output_file, detect_info
	_check = generate_Capture_Lock(globals())
	if _check != None and _check['message'] == 'Fail to open camera !!':
		abort(404, description="Fail to open camera !!")
	else:
		detect_info = _check
	# Send the file as a response
	return send_file(output_file, mimetype='video/webm')

@app.route('/VideoMode/control', methods=['POST'])
def VideoMode_control():
	global File_Export_BOOL, allow_Video_Mode
	data = request.get_json()
	File_Export_BOOL = data['File_Export_BOOL']
	# allow_Video_Mode = data['allow_Video_Mode']
	return jsonify({
		'status': 'VideoMode_control_success',
		# 'allow_Video_Mode': allow_Video_Mode,
		'File_Export_BOOL': File_Export_BOOL
	})

########################## Live Mode
@app.route('/video_feed')
def video_feed():
	global detect_info
	ret_val, detect_info = generate_Live_Lock(globals())
	return Response(ret_val,
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
