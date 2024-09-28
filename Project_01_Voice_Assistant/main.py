import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pywhatkit

# Initialize the recognizer, TTS engine and Female voice
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen and recognize the user's voice
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)
        
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")

    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    
    except sr.RequestError:
        print("Sorry, there seems to be an issue with the service.")
        return ""
    
    return command

# Function to handle time and date requests
def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")

def tell_date():
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")

# Function to search the web
def search_web(query):
    speak(f"Searching the web for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Function to play videos on Youtube 
def play_video_on_youtube(video_name):
    speak(f"Playing {video_name} on YouTube")
    webbrowser.open(f"https://www.youtube.com/results?search_query={video_name}")
    pywhatkit.playonyt(video_name)


# Main function to handle commands
def voice_assistant():
    speak("Hello, I am your voice assistant. How can I help you?")
    
    while True:
        command = listen()

        if "hello" in command or "hi" in command:
            speak("Hello! How can I assist you today?")
        
        elif "time" in command:
            tell_time()
        
        elif "date" in command:
            tell_date()

        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                search_web(query)
            else:
                speak("What do you want me to search for?")
        
        elif "play" in command and "on youtube" in command:
            video_name = command.replace("play", "").replace("on youtube", "").strip()
            if video_name:
                play_video_on_youtube(video_name)
            else:
                speak("Please specify the song or video name.")
        
        elif "exit" in command or "stop" in command:
            speak("Goodbye, Have a nice day!")
            break
        
        else:
            speak("I'm sorry, I don't understand that command.")

# Start the assistant
if __name__ == "__main__":
    voice_assistant()
