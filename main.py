import os
import eel
from backend.auth import recoganize
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import *



def start():
    
    eel.init("frontend") 
    
    play_assistant_sound()
    @eel.expose
    def init():
        eel.hideLoader()
        speak("Jarvisga xush kelibsiz!")
        
        # Yuz tanish qismini vaqtincha o'tkazib yuborish
        try:
            flag = recoganize.AuthenticateFace()
            if flag == 1:
                speak("Yuz muvaffaqiyatli tanildi")
            else:
                speak("Yuz tanish o'tkazib yuborildi")
        except Exception as e:
            print(f"Yuz tanish xatosi: {e}")
            speak("Yuz tanish o'tkazib yuborildi, ovozli yordamchi bilan davom etamiz")
        
        eel.hideFaceAuth()
        eel.hideFaceAuthSuccess()
        speak("Jarvis hizmatingizga tayyor!")
        eel.hideStart()
        play_assistant_sound()
        
    os.system('start msedge.exe --app="http://127.0.0.1:8000/index.html"')
    
    
    
    eel.start("index.html", mode=None, host="localhost", block=True) 

