# Gesture-volume-control
This project demonstrates controlling the system volume using hand gestures, leveraging OpenCV for video capture and MediaPipe for hand tracking.

## Introduction

The Gesture Volume Control system uses computer vision techniques to interpret hand gestures and control the system volume. The primary components of this project are:

1. **OpenCV**: A library for real-time computer vision.
2. **MediaPipe**: A framework by Google for building multimodal (e.g., video, audio, etc.) applied machine learning pipelines, used here for hand tracking.
3. **pycaw**: A library for accessing and manipulating the Windows Core Audio APIs.

## How It Works

1. **Video Capture**: OpenCV captures real-time video from the webcam.
2. **Hand Detection**: MediaPipe processes each video frame to detect hand landmarks.
3. **Gesture Interpretation**: The distance between specific landmarks (e.g., thumb and index finger) is calculated to determine the gesture.
4. **Volume Control**: The gesture is mapped to a volume level, which is then set using pycaw.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- pycaw (for Windows volume control)
- numpy
