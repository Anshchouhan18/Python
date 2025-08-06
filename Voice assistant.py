import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import google.generativeai as genai  # <-- ADDED

# --- CONFIGURATION ---
GEMINI_API_KEY = ""  # <-- PASTE YOUR API KEY HERE

# --- INITIALIZATION ---
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set thresholds for faster recognition
recognizer.energy_threshold = 300  # More sensitive to sound
recognizer.pause_threshold = 0.5   # Shorter pauses between words

# Calibrate ambient noise ONCE during startup
with sr.Microphone() as source:
    print("Calibrating microphone for ambient noise...")
    recognizer.adjust_for_ambient_noise(source, duration=0.5)

# Configure the Gemini API
try:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel('gemini-1.5-flash-latest') 
except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    gemini_model = None

def speak(text):
    """Convert text to speech"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice command and convert it to text (optimized)"""
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return ""

def ask_gemini(prompt):
    """Sends a prompt to the Gemini API and gets a response"""
    if not gemini_model:
        return "The Gemini AI model is not configured. Please check your API key."
    if not prompt:
        return None
    try:
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred with the Gemini API: {e}")
        return "Sorry, I'm having trouble connecting to my brain right now."

def process_command(command):
    """Execute tasks based on the command, falling back to Gemini"""
    
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    
    elif "open camera" in command:
        speak("Opening Camera")
        os.system("start microsoft.windows.camera:")
    
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        exit()
        
    else:
        if command:
            response = ask_gemini(command)
            speak(response)
        else:
            speak("I didn't catch that. Please try again.")

# --- MAIN LOOP ---
if __name__ == "__main__":
    speak("Hello! Say 'Hello' to wake me up.")
    
    while True:
        print("Listening for wake-up command...")
        wake_command = listen()
        
        if "hello" in wake_command:
            speak("Yes, how can I help?")
            command_to_process = listen()
            process_command(command_to_process)
