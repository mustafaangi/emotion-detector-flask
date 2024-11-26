# Emotion Detection Project

## Overview

This project involves emotion detection using a Flask web application. The application uses the Watson NLP Library to analyze text and detect emotions such as anger, disgust, fear, joy, and sadness.


### Files and Directories

- `EmotionDetection/`: This directory contains the emotion detection logic.
  - `__init__.py`: Initializes the EmotionDetection package.
  - `emotion_detection.py`: Contains the `emotion_detector` function that interacts with the Watson NLP Library to detect emotions.
- `server.py`: The Flask web application that provides an endpoint for emotion detection.
- `test_emotion_detection.py`: Unit tests for the `emotion_detector` function.
- `README.md`: This file, providing an overview of the project.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/mustafaangi/emotion-detector-flask.git
   
   cd emotion-detector-flask

   python3 server.py

   curl -X POST http://localhost:5000/emotionDetector -H "Content-Type: application/json" -d '{"text": "I love this new technology."}'

testing:

   python3 -m unittest test_emotion_detection.py