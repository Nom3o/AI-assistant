import os
import speech_recognition as sr
import pyttsx3

# Redirect ALSA warnings
os.environ['PYTHONWARNINGS'] = 'ignore:semaphore_tracker:UserWarning'
os.environ['ALSA_NO_ERROR_LOG'] = '1'

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine with espeak-ng
engine = pyttsx3.init(driverName='espeak')

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        query = listen().lower()
        if "exit" in query:
            speak("Goodbye!")
            break
        else:
            speak(f"You said: {query}")
