import speech_recognition as sr
import pyttsx3
import webbrowser
import os

# text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice command and convert it to text"""
    with sr.Microphone() as source:
        print("Listening for wake-up command...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        try:
            audio = recognizer.listen(source, timeout=10)  # Timeout after 10 sec
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            return ""  # Ignore unrecognized speech
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the internet.")
            return ""

def process_command(command):
    """Execute tasks based on the command"""
    
    if "open google" in command:
        speak("Opening Google")                         # For google
        webbrowser.open("https://www.google.com")
    
    elif "open youtube" in command:
        speak("Opening YouTube")                        # For youtube
        webbrowser.open("https://www.youtube.com")
    
    elif "open instagram" in command:
        speak("Opening Instagram")                      # For instagram
        webbrowser.open("https://www.instagram.com/")
    
    elif "open camera" in command:
        speak("Opening Camera")                         # For camera
        os.system("start microsoft.windows.camera:")
    
    elif "open clock" in command:
        speak("Opening Clock")                          # For clock
        os.system("start ms-clock:")
    
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        exit()                                          # For exit the program 
    
    else:
        speak("Sorry, I don't understand that command.")

# Main loop with wake-up word
if __name__ == "__main__":
    speak("Hello! Say 'Hey dummy' to wake me up.")
    
    while True:
        wake_command = listen()
        if "hey dummy" in wake_command:  # Wake-up word detection
            speak("Yes sir, how can I assist you?")
            
            while True:
                command = listen()
                if command:
                    process_command(command)
                    break  # Return to wake-up listening mode

