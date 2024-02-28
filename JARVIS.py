import pyttsx3
import speech_recognition as sr
import datetime
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You just said: {query}\n")
    except Exception as e:
        print(e)
        speak("Please tell me again")
        query = "none"
    return query

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
       print("Good Morning Riya")
       speak("Good Morning Riya")
    elif hour>=12 and hour<16:
        print("Good Afternoon Riya")
        speak("Good Afternoon Riya")
    elif hour>=16 and hour<20:
        print("Good Evening Riya")
        speak("Good Evening Riya")
    else:
        print("Good Night Riya")
        speak("Good Night Riya")

if __name__ == "__main__":
    wishings()
    query=commands().lower()
    if 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"The current time is {strTime}")
        