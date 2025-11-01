# import playsound
# import eel


# @eel.expose
# def playAssistantSound():
#     music_dir = "frontend\\assets\\audio\\start_sound.mp3"
#     playsound(music_dir)


from compileall import compile_path
import os
import re
from shlex import quote
import struct
import subprocess
import time
import webbrowser
import eel
from hugchat import hugchat 
import pvporcupine
import pyaudio
import pyautogui
import pywhatkit as kit
import pygame
from backend.command import speak
from backend.config import ASSISTANT_NAME
import sqlite3

from backend.helper import extract_yt_term, remove_words
conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()
# Initialize pygame mixer
pygame.mixer.init()

# Define the function to play sound
@eel.expose
def play_assistant_sound():
    # Use a project-relative path so the audio file works across machines
    sound_file = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                              'frontend', 'assets', 'audio', 'start_sound.mp3'))
    if os.path.exists(sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    else:
        print(f"play_assistant_sound: file not found: {sound_file}")
    
    
def openCommand(query):
    query = query.replace(ASSISTANT_NAME,"")
    query = query.replace("open","")
    query = query.replace("kir","")
    app_name = query.strip().lower()

    if app_name != "":
        # Faqat o'zbekcha ilovalar va veb-saytlar
        common_apps = {
            # Veb-saytlar
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "gmail": "https://www.gmail.com",
            
            # Asosiy ilovalar
            "bloknot": "notepad",
            "bloknotga": "notepad",
            "kalkulyator": "calc",
            "hisoblagich": "calc",
            "rasm": "mspaint",
            "chizish": "mspaint",
            
            # Brauzerlar
            "chrome": "chrome",
            "edge": "msedge",
            "firefox": "firefox",
            "brauzer": "msedge",
            
            # Microsoft Office
            "word": "winword",
            "excel": "excel",
            "powerpoint": "powerpnt",
            
            # Boshqa ilovalar
            "skype": "skype",
            "telegram": "telegram",
            "whatsapp": "whatsapp",
            "spotify": "spotify",
            "fayl menejer": "explorer",
            "explorer": "explorer",
            "boshqaruv paneli": "control",
            "control": "control"
        }
        
        try:
            # Umumiy ilova/veb-sayt ekanligini tekshirish
            if app_name in common_apps:
                url_or_app = common_apps[app_name]
                speak(f"{app_name} ochilmoqda")
                
                if url_or_app.startswith("http"):
                    webbrowser.open(url_or_app)
                else:
                    os.system(f'start {url_or_app}')
                return
            
            # Ma'lumotlar bazasidan qidirish
            try:
                cursor.execute( 
                    'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak(f"{app_name} ochilmoqda")
                    os.startfile(results[0][0])
                    return

                cursor.execute(
                    'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak(f"{app_name} ochilmoqda")
                    webbrowser.open(results[0][0])
                    return
            except:
                pass  # Ma'lumotlar bazasi mavjud emas
            
            # Oxirgi imkoniyat: tizim buyrug'i sifatida ochishga harakat qilish
            speak(f"{app_name} ochilmoqda")
            try:
                os.system(f'start {app_name}')
            except:
                speak(f"Kechirasiz, {app_name} topilmadi")
                
        except Exception as e:
            print(f"openCommand xatosi: {e}")
            speak("Kechirasiz, ilovani ochishda xatolik yuz berdi")


def PlayYoutube(query):
    # YouTube da ijro etish uchun qidiruv so'zini ajratish
    original_query = query.lower()
    
    # O'zbekcha va inglizcha so'zlarni olib tashlash
    words_to_remove = [
        "youtube", "da", "ijro", "et", "play", "on", "qo'shiq", "music", 
        "song", "video", "kir", "open", "ochish", "tinglash", "listen"
    ]
    
    search_term = original_query
    for word in words_to_remove:
        search_term = search_term.replace(word, "")
    
    # Ortiqcha bo'shliqlarni olib tashlash
    search_term = " ".join(search_term.split())
    
    if search_term:
        # O'zbekcha yoki inglizcha javob
        if any(uz_word in original_query for uz_word in ["da", "ijro", "qo'shiq"]):
            speak(f"YouTube da {search_term} ijro etilmoqda")
        else:
            speak(f"Playing {search_term} on YouTube")
        
        try:
            print(f"Qidiruv so'zi: {search_term}")
            kit.playonyt(search_term)
        except Exception as e:
            print(f"YouTube xatosi: {e}")
            if any(uz_word in original_query for uz_word in ["da", "ijro", "qo'shiq"]):
                speak("YouTube da ijro etishda xatolik yuz berdi")
            else:
                speak("Error playing on YouTube")
    else:
        # Agar qidiruv so'zi bo'lmasa, YouTube ni ochish
        if any(uz_word in original_query for uz_word in ["da", "ijro", "qo'shiq"]):
            speak("YouTube ochilmoqda")
        else:
            speak("Opening YouTube")
        try:
            webbrowser.open("https://www.youtube.com")
        except:
            speak("YouTube ochishda xatolik yuz berdi")


def hotword():
    import speech_recognition as sr
    
    print("Jarvis ovozli yordamchi ishga tushdi. 'Jarvis' deb ayting...")
    r = sr.Recognizer()
    
    while True:
        try:
            with sr.Microphone(device_index=1) as source:
                print("'Jarvis' so'zini tinglayapman...")
                r.energy_threshold = 300
                r.pause_threshold = 0.8
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
            
            try:
                text = r.recognize_google(audio, language='en-US').lower()
                print(f"Heard: {text}")
                
                if "jarvis" in text:
                    print("Jarvis hotword detected! Activating voice assistant...")
                    
                    # pressing shorcut key win+j
                    import pyautogui as autogui
                    autogui.keyDown("win")
                    autogui.press("j")
                    time.sleep(2)
                    autogui.keyUp("win")
                    
            except sr.UnknownValueError:
                pass  # No speech detected, continue listening
            except sr.RequestError as e:
                print(f"Speech recognition error: {e}")
                time.sleep(1)
                
        except sr.WaitTimeoutError:
            pass  # Timeout, continue listening
        except Exception as e:
            print(f"Hotword detection error: {e}")
            time.sleep(1)


def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT Phone FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
    
    
def whatsApp(Phone, message, flag, name):
    

    if flag == 'message':
        target_tab = 12
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        jarvis_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={Phone}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)


def chatBot(query):
    user_input = query.lower()
    
    # Faqat o'zbekcha javoblar
    responses = {
        "salom": "Salom! Men Jarvis, sizning yordamchingizman. Sizga qanday yordam bera olaman?",
        "hello": "Salom! Men Jarvis, sizning yordamchingizman. Sizga qanday yordam bera olaman?",
        "hi": "Salom! Men Jarvis. Bugun sizga qanday yordam bera olaman?",
        "qalaysiz": "Men yaxshiman, rahmat! Sizga qanday yordam bera olaman?",
        "yaxshimisiz": "Ha, men yaxshiman! Sizga qanday xizmat qila olaman?",
        "ismingiz nima": "Mening ismim Jarvis. Men sizning shaxsiy yordamchingizman.",
        "siz kimsiz": "Men Jarvis, sizning AI yordamchingizman. Turli vazifalar bilan yordam bera olaman.",
        "rahmat": "Arzimaydi! Yana biror narsa kerakmi?",
        "thank you": "Arzimaydi! Yana biror narsa kerakmi?",
        "thanks": "Arzimaydi! Yana biror narsa kerakmi?",
        "xayr": "Xayr! Yaxshi kun o'tkazing!",
        "bye": "Xayr! Yaxshi kun o'tkazing!",
        "goodbye": "Xayr! Yaxshi kun o'tkazing!",
        "yaxshi tong": "Xayrli tong! Bugun sizga qanday yordam bera olaman?",
        "good morning": "Xayrli tong! Bugun sizga qanday yordam bera olaman?",
        "yaxshi kech": "Xayrli kech! Nima qila olaman?",
        "good evening": "Xayrli kech! Nima qila olaman?",
        "soat necha": f"Hozir soat {time.strftime('%H:%M:%S')}",
        "what time": f"Hozir soat {time.strftime('%H:%M:%S')}",
        "bugun qaysi kun": f"Bugun {time.strftime('%A, %B %d, %Y')}",
        "what day": f"Bugun {time.strftime('%A, %B %d, %Y')}",
        "nima qila olasiz": "Men sizga ilovalar ochish, YouTube da musiqa ijro etish, qo'ng'iroq qilish va suhbatlashishda yordam bera olaman!",
        "what can you do": "Men sizga ilovalar ochish, YouTube da musiqa ijro etish, qo'ng'iroq qilish va suhbatlashishda yordam bera olaman!",
        "yordam": "Albatta! Men sizga quyidagilar bilan yordam bera olaman: ilovalar ochish, YouTube da qo'shiq ijro etish, qo'ng'iroq qilish. Nima kerak?",
        "help": "Albatta! Men sizga quyidagilar bilan yordam bera olaman: ilovalar ochish, YouTube da qo'shiq ijro etish, qo'ng'iroq qilish. Nima kerak?",
        "yaxshi": "Yaxshi! Sizga qanday yordam kerak?",
        "great": "Yaxshi! Sizga qanday yordam kerak?",
        "zo'r": "Zo'r! Men sizga qanday xizmat qila olaman?",
        "awesome": "Zo'r! Men sizga qanday xizmat qila olaman?",
        "ajoyib": "Ajoyib! Nima qilishni xohlaysiz?",
        "cool": "Ajoyib! Nima qilishni xohlaysiz?",
        "menga yordam ber": "Albatta! Sizga qanday yordam kerak? Men ilovalar ochish, musiqa ijro etish yoki suhbatlashishda yordam bera olaman.",
        "help me": "Albatta! Sizga qanday yordam kerak? Men ilovalar ochish, musiqa ijro etish yoki suhbatlashishda yordam bera olaman.",
        "nima qilyapsan": "Men sizning buyruqlaringizni kutayapman. Sizga qanday yordam bera olaman?",
        "what are you doing": "Men sizning buyruqlaringizni kutayapman. Sizga qanday yordam bera olaman?",
        "ishlaydimi": "Ha, men ishlayapman! Sizga qanday yordam kerak?",
        "are you working": "Ha, men ishlayapman! Sizga qanday yordam kerak?",

    }
    
    # Aniq moslikni tekshirish (o'xshash so'zlarni ham qo'shamiz)
    for key, response in responses.items():
        if key in user_input or (key == "salom" and ("salon" in user_input)):
            print(f"Javob: {response}")
            speak(response)
            return response
    
    # Qo'shimcha umumiy javoblar
    if any(word in user_input for word in ["nima", "what", "qanday", "how"]):
        response = "Men sizga turli xil yordam bera olaman. Ilovalar ochish, YouTube da musiqa tinglash, yoki oddiy suhbatlashish mumkin. Nima kerak?"
        print(f"Umumiy javob: {response}")
        speak(response)
        return response
    
    # Agar hech narsa topilmasa, do'stona o'zbekcha javob
    response = "Kechirasiz, sizni to'liq tushunmadim. Iltimos, aniqroq ayting. Men sizga ilovalar ochish, YouTube da musiqa ijro etish yoki oddiy suhbatlashishda yordam bera olaman."
    
    print(f"Tushunmadim javob: {response}")
    speak(response)
    return response