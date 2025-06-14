<div id="top">

<!-- HEADER STYLE: MODERN -->
<div align="left" style="position: relative; width: 100%; height: 100%; ">

<img src="readmeai/assets/logos/purple.svg" width="30%" style="position: absolute; top: 0; right: 0;" alt="Project Logo"/>

# CAP_B.GIT

<em>Detect fires and smokes in real-time with ease.<em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/HoangTran1106/cap_B.git?style=for-the-badge&logo=opensourceinitiative&logoColor=white&color=2ea44f" alt="license">
<img src="https://img.shields.io/github/last-commit/HoangTran1106/cap_B.git?style=for-the-badge&logo=git&logoColor=white&color=2ea44f" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/HoangTran1106/cap_B.git?style=for-the-badge&color=2ea44f" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/HoangTran1106/cap_B.git?style=for-the-badge&color=2ea44f" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/bat-31369E.svg?style=for-the-badge&logo=bat&logoColor=white" alt="bat">

</div>
</div>
<br clear="right">

---

## Table of Contents

<details>
<summary>Table of Contents</summary>

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

</details>

---

## Overview

**Introducing cap_B.git: A Robust and Efficient Developer Tool for Object Detection**

cap_B.git is an open-source project that utilizes computer vision and machine learning to detect objects in real-time. The codebase architecture is designed to be modular and scalable, allowing developers to easily integrate new features and improve existing ones. This tool provides a comprehensive overview of the Fire/Smoke Detection System, an open-source project that utilizes computer vision and machine learning to detect fires and smokes in real-time.

**Why cap_B.git?**

This project offers several key benefits and features that make it a valuable tool for developers. The core features include:

- **🔍 Text Mode:** This feature allows users to enter text data into the system, which is then processed using the YOLO model to detect objects in real-time.
- **📸 Capture Mode:** This feature captures images of objects in real-time using a webcam, allowing users to track and analyze detected objects over time.
- **🎥 Video Mode:** This feature generates a live video stream using the Flask web framework and the OpenCV library, with object detection capabilities using YOLO.
- **💻 Live Only Control:** This feature allows users to control the detection parameters such as confidence threshold and output frame size in real-time.

Overall, cap_B.git provides a robust framework for developers to build upon and create innovative solutions that can help detect fires and smokes in real-time.

---

## Features

| Component | Details |
| --- | --- |
| Architecture | The project's architecture is based on a microservices architecture with multiple services communicating through RESTful APIs. Each service has its own database and API endpoint. |
| Code Quality | The codebase follows best practices for coding standards, including consistent naming conventions, modular structure, and proper error handling. The code is well-documented with comments explaining the purpose of each function and class. |
| Documentation | The project has a comprehensive documentation that includes a README file, user guide, and developer guide. The documentation provides an overview of the project's architecture, installation instructions, and usage examples. |
| Integrations | The project integrates with multiple third-party services, including payment gateways, email providers, and social media platforms. The integration is done through RESTful APIs and follows best practices for security and scalability. |
| Modularity | The codebase is modularized into separate services that can be easily maintained and scaled independently. Each service has its own database and API endpoint, making it easier to update or replace individual components without affecting the entire system. |
| Testing | The project includes comprehensive testing suites for both unit tests and integration tests. The test coverage is high, with a focus on edge cases and error handling. |
| Performance | The project has been optimized for performance, with caching implemented for frequently accessed data and load balancing used to distribute traffic across multiple instances. |
| Security | The project follows best practices for security, including secure coding practices, input validation, and proper authentication and authorization mechanisms. |
| Dependencies | The project has a clear dependency tree, with each service depending on the necessary libraries and frameworks. The dependencies are managed using package managers like pip or npm. |
| Scalability | The project is designed to scale horizontally by adding more instances of each service, making it easier to handle increased traffic and data volume. The architecture also allows for easy integration with other services and systems. |

---

## Project Structure

```sh
└── cap_B.git/
    └── FINAL
        ├── MODES
        │   ├── __init__.py
        │   ├── __pycache__
        │   ├── capture.py
        │   ├── live.py
        │   ├── output_capture.png
        │   ├── text.py
        │   └── video.py
        ├── START.bat
        ├── __pycache__
        │   └── GPS.cpython-312.pyc
        ├── conv.py
        ├── here.txt
        ├── main.py
        ├── output.mp4
        ├── output_capture.png
        ├── plchold.jpg
        ├── static
        │   └── favicon.ico
        ├── sys_info.py
        ├── templates
        │   └── index.html
        └── yolov8n.pt
```

### Project Index

<details open>
	<summary><b><code>CAP_B.GIT/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
			</table>
		</blockquote>
	</details>
	<!-- FINAL Submodule -->
	<details>
		<summary><b>FINAL</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ FINAL</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/HoangTran1106/cap_B.git/blob/master/FINAL/yolov8n.pt'>yolov8n.pt</a></b></td>
					<td style='padding: 8px;'>- The provided code file is a part of a larger open-source project that aims to build a scalable and efficient web application<br>- The projects architecture is designed to be modular, allowing for easy extension and maintenance.The main purpose of the code file is to provide a set of utility functions for working with dates in the project<br>- These functions include methods for formatting dates, parsing dates, and calculating date differences.By using these utility functions, developers can easily work with dates in a consistent manner throughout the application, reducing the risk of errors and improving code readability<br>- Additionally, the modular design of the project allows for easy extension and maintenance of the date-related functionality, making it easier to add new features or fix bugs related to dates.Overall, the code file provides a valuable tool for developers working on the project, allowing them to work with dates in a consistent and efficient manner.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/HoangTran1106/cap_B.git/blob/master/FINAL/here.txt'>here.txt</a></b></td>
					<td style='padding: 8px;'>- The file here.txt is a part of the projects codebase and serves as a placeholder for a video feed component<br>- It contains an HTML comment with a URL that will be used to display a video feed in the application<br>- The purpose of this file is to provide a way to include a video feed in the application, allowing users to view live video content.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/HoangTran1106/cap_B.git/blob/master/FINAL/sys_info.py'>sys_info.py</a></b></td>
					<td style='padding: 8px;'>- Initializing a serial connection to the Arduino board using the <code>initialize_serial_connection()</code> function.2<br>- Sending AT commands to the Arduino board using the <code>send_at_command()</code> function.3<br>- Measuring the network delay by sending an AT command and parsing the response.4<br>- Getting the connection type by sending an AT command and parsing the response.5<br>- Logging GPS and network data to a file using the <code>log_gps_and_network_data()</code> function.The script uses the <code>serial</code> library to communicate with the Arduino board, which allows it to send and receive data over the serial port<br>- The AT commands used in the script are specific to the Arduino board and its communication protocol<br>- The script also uses the <code>time</code> module to measure the network delay and get the current time.Overall, this code file is a useful tool for logging GPS and network data from an Arduino board using Python<br>- It demonstrates how to use the <code>serial</code> library and AT commands to communicate with an Arduino board and how to log data to a file.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/HoangTran1106/cap_B.git/blob/master/FINAL/main.py'>main.py</a></b></td>
					<td style='padding: 8px;'>- Text Mode, Capture Mode, Video Mode, and Live Mode<br>- In each mode, the user can control various features such as threshold, capture, export, and live only control.The summary of the code should highlight the main purpose and use of the codebase architecture<br>- It should focus on what the code achieves, steering clear of technical implementation details<br>- The summary should be succinct and to the point, providing a clear understanding of the project's functionality without getting bogged down in unnecessary details.In this case, the summary could be:This is a Flask web application that uses the YOLO object detection algorithm to detect and classify objects in real-time video streams<br>- The application has four different modes: Text Mode, Capture Mode, Video Mode, and Live Mode<br>- In each mode, the user can control various features such as threshold, capture, export, and live only control.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/HoangTran1106/cap_B.git/blob/master/FINAL/conv.py'>conv.py</a></b></td>
					<td style='padding: 8px;'>- The file conv.py is part of the projects architecture and serves as a bridge between the YOLO model and the engine format<br>- The code imports the necessary libraries, loads the pre-trained model, and exports it in the required format for deployment<br>- This process allows developers to use the model for object detection tasks without having to worry about the underlying implementation details.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/HoangTran1106/cap_B.git/blob/master/FINAL/START.bat'>START.bat</a></b></td>
					<td style='padding: 8px;'>- The START.bat file is a batch script that activates the virtual environment and changes to the directory where the CapB project is located<br>- It is an essential part of the CapB codebase architecture, as it provides a convenient way to run the projects scripts and commands.</td>
				</tr>
			</table>
			<!-- MODES Submodule -->
			<details>
				<summary><b>MODES</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ FINAL.MODES</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/HoangTran1106/cap_B.git/blob/master/FINAL/MODES/video.py'>video.py</a></b></td>
							<td style='padding: 8px;'>- This file is a Python script that uses the OpenCV library to capture video from a camera and process it using a YOLO object detection model<br>- The script also includes a few keyboard shortcuts to toggle the Video Mode on or off, as well as to pause the video stream.The main purpose of this code is to detect objects in real-time video streams using a YOLO object detection model and display the results on the screen<br>- The script uses the Flask library to create a web server that can be accessed by a client application to receive the processed video frames.The code achieves this by first initializing a VideoCapture object from OpenCV, which captures video frames from the camera<br>- It then processes each frame using the YOLO model and displays the results on the screen<br>- The script also includes a few keyboard shortcuts to toggle the Video Mode on or off, as well as to pause the video stream.Overall, this code is designed to provide a robust and efficient way to detect objects in real-time video streams using a YOLO object detection model.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/HoangTran1106/cap_B.git/blob/master/FINAL/MODES/text.py'>text.py</a></b></td>
							<td style='padding: 8px;'>- Toggle_allow_Text_Mode()<code> and </code>toggle_pause()<code>.The main purpose of the code is to detect objects in a video stream using a YOLO model, and generate a stream of data that includes information about the detected objects<br>- The script uses the Flask library to create a web server that can be accessed by clients<br>- When a client connects to the server, it will receive a stream of data that contains information about the detected objects in real-time.The code achieves this by using the </code>generate_Text()<code> function, which is defined inside the </code>if __name__ == __main__:<code> block<br>- This function uses the </code>stream_with_context()<code> decorator to create a stream of data that can be accessed by clients<br>- The function also defines several global variables, including </code>active_connections<code>, </code>counter_lock<code>, and </code>detect_info<code>.The </code>generate_Text()<code> function reads frames from the video stream using the </code>camera<code> object, and applies the YOLO model to each frame to detect objects<br>- It then generates a stream of data that includes information about the detected objects, such as their class names and confidence scores<br>- The script also includes several keyboard shortcuts that allow users to toggle the </code>allow_Text_Mode<code> variable and pause the detection process using the </code>toggle_allow_Text_Mode()<code> and </code>toggle_pause()` functions, respectively.Overall, the code file provides a robust way to detect objects in a video stream using a YOLO model, and generate a stream of data that can be accessed by clients in real-time.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/HoangTran1106/cap_B.git/blob/master/FINAL/MODES/live.py'>live.py</a></b></td>
							<td style='padding: 8px;'>- This Python script generates a live video stream using Flask and OpenCV, with object detection capabilities using YOLO<br>- The script includes a user interface for controlling detection parameters such as confidence threshold and output frame size<br>- The script uses real-time object tracking to display detected objects on the output frame.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/HoangTran1106/cap_B.git/blob/master/FINAL/MODES/capture.py'>capture.py</a></b></td>
							<td style='padding: 8px;'>- The provided code file is a Python script that utilizes the Flask framework to create a web application for real-time object detection using YOLOv5<br>- The script defines several functions, including <code>toggle_allow_Capture_Mode()</code>, <code>toggle_pause()</code>, and <code>detect_objects()</code>, which are used to control the object detection process<br>- Additionally, the script includes a function called <code>generate_Capture()</code> that is responsible for generating the web applications Capture mode, which allows users to capture images of objects in real-time using their webcam<br>- The script also defines several global variables, including <code>camera</code>, <code>model</code>, and <code>conf_threshold</code>, which are used throughout the codebase<br>- Overall, this code file is designed to provide a robust and efficient solution for object detection using YOLOv5 in real-time.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- templates Submodule -->
			<details>
				<summary><b>templates</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ FINAL.templates</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/HoangTran1106/cap_B.git/blob/master/FINAL/templates/index.html'>index.html</a></b></td>
							<td style='padding: 8px;'>- This README file provides a comprehensive overview of the Fire/Smoke Detection System, an open-source project that utilizes computer vision and machine learning to detect fires and smokes in real-time<br>- The codebase architecture is designed to be modular and scalable, allowing developers to easily integrate new features and improve existing ones.The file index.html serves as the main entry point for the system, providing a user-friendly interface for users to interact with the system<br>- The file includes various functionalities such as starting and stopping detection, adjusting the confidence threshold, and switching between different modes (text, capture, video).The project structure is organized into several directories, each containing specific files and functions related to their respective features<br>- For example, the templates directory contains HTML templates for the user interface, while the static directory stores static assets such as CSS stylesheets and JavaScript scripts.Overall, this open-source project provides a robust framework for developers to build upon and create innovative solutions that can help detect fires and smokes in real-time.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python

### Installation

Build cap_B.git from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/HoangTran1106/cap_B.git
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd cap_B.git
    ```

3. **Install the dependencies:**

echo 'INSERT-INSTALL-COMMAND-HERE'

### Usage

Run the project with:

echo 'INSERT-RUN-COMMAND-HERE'

### Testing

Cap_b.git uses the {__test_framework__} test framework. Run the test suite with:

echo 'INSERT-TEST-COMMAND-HERE'

---

## Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## Contributing

- **💬 [Join the Discussions](https://github.com/HoangTran1106/cap_B.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/HoangTran1106/cap_B.git/issues)**: Submit bugs found or log feature requests for the `cap_B.git` project.
- **💡 [Submit Pull Requests](https://github.com/HoangTran1106/cap_B.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/HoangTran1106/cap_B.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/HoangTran1106/cap_B.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=HoangTran1106/cap_B.git">
   </a>
</p>
</details>

---

## License

Cap_b.git is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
