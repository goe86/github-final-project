from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector
app= Flask(__name__)

@app.route("/emotionDetector/<text>")
def evaluate_emotion(text):
    result=emotion_detector(text)
    formatted_str= f"For the given statment, the system response is 'anger': {result['anger']},'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}"
    return formatted_str


if __name__== "__main__":
    app.run(debug=True)
