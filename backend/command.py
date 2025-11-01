import time
import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # Pick a voice safely (fall back to first available)
    try:
        voice_to_use = voices[2].id if len(voices) > 2 else voices[0].id
    except Exception:
        voice_to_use = voices[0].id if voices else None
    if voice_to_use:
        engine.setProperty('voice', voice_to_use)
    engine.setProperty('rate', 174)
    
    # Try to use eel functions if available
    try:
        eel.DisplayMessage(text)
    except:
        pass  # eel not initialized, skip
    
    engine.say(text)
    engine.runAndWait()
    
    try:
        eel.receiverText(text)
    except:
        pass  # eel not initialized, skip

# Expose the Python function to JavaScript

def takecommand():
    r = sr.Recognizer()
    # Eng yaxshi ishlayotgan mikrofonni ishlatamiz
    with sr.Microphone(device_index=1) as source:
        print("Tinglayapman...")
        try:
            eel.DisplayMessage("Tinglayapman...")
        except:
            pass
        r.energy_threshold = 300
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=10, phrase_time_limit=5)

    try:
        print("Taniyapman...")
        try:
            eel.DisplayMessage("Taniyapman...")
        except:
            pass
        
        # Avval ingliz tilida, keyin rus tilida urinib ko'ramiz
        try:
            query = r.recognize_google(audio, language='en-US')
        except:
            try:
                query = r.recognize_google(audio, language='ru-RU')
            except:
                query = r.recognize_google(audio, language='uz-UZ')
        
        print(f"Siz aytdingiz: {query}\n")
        try:
            eel.DisplayMessage(query)
        except:
            pass
        
        return query.lower()
    except Exception as e:
        print(f"Xato: {str(e)}\n")
        return None



@eel.expose
def takeAllCommands(message=None):
    if message is None:
        query = takecommand()  # If no message is passed, listen for voice input
        if not query:
            return  # Exit if no query is received
        print(f"Voice command received: {query}")
        try:
            eel.senderText(query)
        except:
            pass
    else:
        query = message  # If there's a message, use it
        print(f"Text message received: {query}")
        try:
            eel.senderText(query)
        except:
            pass
    
    try:
        if query:
            query = query.lower()
            if "open" in query or "kir" in query or "launch" in query or "start" in query:
                from backend.feature import openCommand
                openCommand(query)
            elif "send message" in query or "call" in query or "video call" in query or "xabar yuborish" in query or "qo'ng'iroq" in query or "message" in query:
                from backend.feature import findContact, whatsApp
                flag = ""
                Phone, name = findContact(query)
                if Phone != 0:
                    if "send message" in query:
                        flag = 'message'
                        speak("What message to send?")
                        query = takecommand()  # Ask for the message text
                    elif "call" in query:
                        flag = 'call'
                    else:
                        flag = 'video call'
                    whatsApp(Phone, query, flag, name)
            elif ("youtube" in query and ("play" in query or "ijro" in query or "qo'shiq" in query)) or \
                 ("play" in query and ("youtube" in query or "music" in query or "song" in query)) or \
                 ("ijro et" in query) or ("qo'shiq" in query and "youtube" in query):
                from backend.feature import PlayYoutube
                PlayYoutube(query)
            else:
                from backend.feature import chatBot
                chatBot(query)
        else:
            speak("No command was given.")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, something went wrong.")
    
    try:
        eel.ShowHood()
    except:
        pass
