'''import time
import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("FRIDAY: I'm listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"FRIDAY: You said '{command}'")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
            return None
        except sr.RequestError:
            speak("Sorry, I'm having trouble reaching the speech recognition service.")
            return None


# Simulating voice command processing
def process_voice_command(command):
    
    else:
        speak("I'm sorry, I can't assist with that command.")

# Example of how to use the function
if __name__ == "__main__":
    speak("What can I help you with today?")
    voice_command = listen()
    if voice_command:
        process_voice_command(voice_command)

import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

import time
from datetime import datetime, timedelta
import threading

# Function to speak reminders
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to set a reminder
def set_reminder(reminder_time, reminder_message):
    def reminder():
        time.sleep(reminder_time)
        speak(f"Reminder: {reminder_message}")
        print(f"Reminder: {reminder_message}")
    
    # Run the reminder in a separate thread to not block the main program
    reminder_thread = threading.Thread(target=reminder)
    reminder_thread.start()

# Function to handle reminder input
def handle_reminder():
    speak("What should I remind you about?")
    reminder_message = takeCommand()
    
    speak("In how many minutes should I remind you?")
    minutes = int(takeCommand())
    
    reminder_time = minutes * 60  # Convert minutes to seconds
    set_reminder(reminder_time, reminder_message)
    speak(f"Reminder set for {minutes} minutes.")

# Example usage inside your main loop:
if 'set reminder' in query:
    handle_reminder()
'''
