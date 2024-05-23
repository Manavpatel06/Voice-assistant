import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("User:", command)
            return command.lower()
        except sr.UnknownValueError:
            #speak("Sorry, I didn't catch that. Please try again.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down. Please try again later.")
            return ""

def get_current_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_current_date():
    return datetime.datetime.now().strftime("%B %d, %Y")

def search_web(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "time" in command:
        current_time = get_current_time()
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = get_current_date()
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        speak("What do you want to search for?")
        query = listen()
        if query:
            speak(f"Searching for {query}")
            search_web(query)
    elif "bye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't catch that. Please try again.")

speak("Welcome! I am your Assistant.")
while True:
    command = listen()
    handle_command(command)

