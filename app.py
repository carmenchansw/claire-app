from flask import Flask, jsonify
from flask_cors import CORS
import speech_recognition as sr

app = Flask(__name__)
CORS(app) # This allows your index.html to talk to this script

@app.route('/transcribe', methods=['GET'])
def transcribe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            # Using Whisper to turn voice to text
            text = r.recognize_whisper(audio, model="tiny")
            return jsonify({"status": "success", "text": text})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(port=5000)