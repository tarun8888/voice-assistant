#voice assistant using python

import datetime
import pyttsx3
import speech_recognition as sr 
import wikipedia
import webbrowser 
import os 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")
    
    elif hour >= 16 and hour< 20:
        speak("Good Evening!")
    else: 
        speak("Good Night!!")

    speak("how can I help you? ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("recognising...")
            query = r.recognize_google(audio,language='en-in')
            print("you said: ", query)
            

        except Exception as e:
            print(e)
            print("speak again...")
            speak("speak again...")
            return "None"
    return query

if __name__== "__main__" :
    while True:
        query = takeCommand().lower()
        if query == 'hi' or query =='hello':
            speak("hello master!")
            wishMe()

        elif 'wikipedia' in query:
            speak("searching wikipedia...")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")  

        elif 'open amazon prime video' in query:
            webbrowser.open("primevideo.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

