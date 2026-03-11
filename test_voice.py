import whisper
import speech_recognition as sr

def transcribe_from_mic():
    # 1. Initialize the recognizer
    r = sr.Recognizer()
    
    # 2. Use the microphone as the source
    with sr.Microphone() as source:
        print("Adjusting for background noise... please wait.")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening... speak now!")
        
        # Capture the audio
        audio = r.listen(source)
        print("Processing with Whisper...")

    try:
        # 3. Use Whisper to transcribe the audio locally
        # 'tiny' is the fastest model; 'base' is slightly more accurate
        text = r.recognize_whisper(audio, model="tiny")
        print(f"You said: {text}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    transcribe_from_mic()