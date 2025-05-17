"""
Flask web application for detecting emotions in user text.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Renders the home page with the input form.
    Returns:
        str: Rendered HTML page
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Handles emotion detection from user input.
    Returns:
        JSON: Resulting message with emotions or error
    """
    text_to_analyze = request.form.get("text")

    if not text_to_analyze:
        return jsonify({"message": "Invalid text! Please try again!"})

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return jsonify({"message": "Invalid text! Please try again!"})

    response = (
        f"For the given statement, the system response is "
        f"anger: {result['anger']}, "
        f"disgust: {result['disgust']}, "
        f"fear: {result['fear']}, "
        f"joy: {result['joy']}, "
        f"sadness: {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"message": response})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
