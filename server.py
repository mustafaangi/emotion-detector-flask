"""
Flask application for emotion detection.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Endpoint to detect emotions in the provided text.
    """
    data = request.get_json()
    text_to_analyze = data.get('text')
    if not text_to_analyze:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return jsonify({"response": "Invalid text! Please try again."})

    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    