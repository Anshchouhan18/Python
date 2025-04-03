# import speech_recognition as sr
# import pyttsx3
# import webbrowser
# import os

# # Initialize recognizer and text-to-speech engine
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def speak(text):
#     """Convert text to speech"""
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     """Capture voice command and convert it to text"""
#     with sr.Microphone() as source:
#         print("Listening for wake-up command...")
#         recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
#         try:
#             audio = recognizer.listen(source, timeout=10)  # Timeout after 10 sec
#             command = recognizer.recognize_google(audio).lower()
#             print(f"You said: {command}")
#             return command
#         except sr.UnknownValueError:
#             return ""  # Ignore unrecognized speech
#         except sr.RequestError:
#             speak("Sorry, I'm having trouble connecting to the internet.")
#             return ""

# def process_command(command):
#     """Execute tasks based on the command"""
    
#     if "open google" in command:
#         speak("Opening Google")                         # For google
#         webbrowser.open("https://www.google.com")
    
#     elif "open youtube" in command:
#         speak("Opening YouTube")                        # For youtube
#         webbrowser.open("https://www.youtube.com")
    
#     elif "open instagram" in command:
#         speak("Opening Instagram")                      # For instagram
#         webbrowser.open("https://www.instagram.com/")
    
#     elif "open camera" in command:
#         speak("Opening Camera")                         # For comera
#         os.system("start microsoft.windows.camera:")
    
#     elif "open clock" in command:
#         speak("Opening Clock")                          # For clock
#         os.system("start ms-clock:")
    
#     elif "exit" in command or "bye" in command:
#         speak("Goodbye!")
#         exit()                                          # For exit the program 
    
#     else:
#         speak("Sorry, I don't understand that command.")

# # Main loop with wake word
# if __name__ == "__main__":
#     speak("Hello! Say 'Hey dummy' to wake me up.")
    
#     while True:
#         wake_command = listen()
#         if "hey dummy" in wake_command:  # Wake word detection
#             speak("Yes sir, how can I assist you?")
            
#             while True:
#                 command = listen()
#                 if command:
#                     process_command(command)
#                     break  # Return to wake-up listening mode

import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import requests

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# DeepSeek API configuration
DEEPSEEK_API_KEY = "YOUR_DEEPSEEK_API_KEY"  # Replace with your actual API key
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

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

def handle_general_query(query):
    """Handle general queries using DeepSeek API"""
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY == "YOUR_DEEPSEEK_API_KEY":
        return "API key is missing. Please update your DeepSeek API key."

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": query}],
        "temperature": 0.7
    }
    
    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        print("API Response:", result)  # Debugging: Print response to check structure

        # Extract text response correctly
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0].get("text", "I'm not sure about that.")
        else:
            return "I didn't understand the response from the server."

    except requests.exceptions.RequestException as e:
        print(f"API Request Error: {e}")
        return "Sorry, I'm having trouble connecting to the knowledge base."

def process_command(command):
    """Execute tasks based on the command"""
    
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    
    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com/")
    
    elif "open camera" in command:
        speak("Opening Camera")
        os.system("start microsoft.windows.camera:")
    
    elif "open clock" in command:
        speak("Opening Clock")
        os.system("start ms-clock:")
    
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        exit()
    
    else:
        # Handle general queries with DeepSeek
        speak("Let me think about that...")
        api_response = handle_general_query(command)
        speak(api_response)

# Main loop with wake word
if __name__ == "__main__":
    speak("Hello! Say 'Hey dummy' to wake me up.")
    
    while True:
        wake_command = listen()
        if "hey dummy" in wake_command:  # Wake word detection
            speak("Yes sir, how can I assist you?")
            
            while True:
                command = listen()
                if command:
                    process_command(command)
                    break  # Return to wake-up listening mode
