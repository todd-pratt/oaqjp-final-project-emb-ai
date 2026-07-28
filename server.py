"""This module demonstrates a simple server."""

import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

my_app = Flask("My Emotion Detection Application")


@my_app.route('/')
# Define method for default route
# This method is to return the default page
def get_index():
    """Return default route."""
    return render_template('index.html')

@my_app.route('/emotionDetector')
# Define a method emotionDetector route
# This method is to return the emotion detector
def get_emotion_detector():
    """Return emotion detection text."""
    query = request.args.get("textToAnalyze")
    resp = emotion_detector(query)
    if resp["dominant_emotion"] == "None":
        return "Invalid text! Please try again!"

    dominant = resp["dominant_emotion"]
    dominant = dominant.replace("\"", "")

    resp.pop("dominant_emotion")
    resp_text = json.dumps(resp)
    resp_text = resp_text.replace("\"", "'")
    resp_text = resp_text.replace("{", "")
    resp_text = resp_text.replace("}", "")

    return (
        f"For the given statement, the system response is {resp_text}."
        " The dominant emotion is {dominant}."
    )
