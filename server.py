"""
Flask server for Emotion Detection Web Application
"""

# Import Flask modules
from flask import Flask, render_template, request

# Import emotion detector function from package
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask application
app = Flask(__name__)


# Route for homepage
@app.route("/")
def render_index_page():
    """
    Render the main HTML page
    """
    return render_template('index.html')


# REQUIRED ROUTE (as per instruction)
@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Calls emotion detector and formats output
    """

    # Get text entered by user
    text_to_analyze = request.args.get('textToAnalyze')

    # Call emotion detection function
    response = emotion_detector(text_to_analyze)

    # Handle invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Format output exactly as required
    output = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return output


# Run application on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    