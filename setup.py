"""
Jarvis O'zbekcha Ovozli Yordamchi - Setup Script
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Python versiyasini tekshirish"""
    if sys.version_info < (3, 8):
        print("❌ Xato: Python 3.8 yoki undan yuqori versiya kerak!")
        print(f"Sizda: Python {sys.version}")
        return False
    print(f"✅ Python versiyasi: {sys.version}")
    return True

def check_os():
    """Operatsion tizimni tekshirish"""
    os_name = platform.system()
    if os_name != "Windows":
        print(f"⚠️  Ogohlantirish: Bu dastur Windows uchun optimallashtirilgan. Sizda: {os_name}")
    else:
        print(f"✅ Operatsion tizim: {os_name}")
    return True

def install_requirements():
    """Kerakli paketlarni o'rnatish"""
    print("\n📦 Kerakli paketlarni o'rnatish...")
    try:
        # pip ni yangilash
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        
        # requirements.txt dan o'rnatish
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        
        print("✅ Barcha paketlar muvaffaqiyatli o'rnatildi!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Paketlarni o'rnatishda xato: {e}")
        return False

def test_microphone():
    """Mikrofonni test qilish"""
    print("\n🎤 Mikrofonni test qilish...")
    try:
        import speech_recognition as sr
        r = sr.Recognizer()
        
        # Mikrofonlarni ro'yxatlash
        print("Mavjud mikrofonlar:")
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print(f"  {index}: {name}")
        
        # Birinchi mikrofonni test qilish
        with sr.Microphone() as source:
            print("Mikrofon sozlanmoqda...")
            r.adjust_for_ambient_noise(source, duration=1)
        
        print("✅ Mikrofon tayyor!")
        return True
    except Exception as e:
        print(f"❌ Mikrofon xatosi: {e}")
        return False

def create_startup_script():
    """Ishga tushirish skriptini yaratish"""
    print("\n📝 Ishga tushirish skriptini yaratish...")
    
    current_dir = os.getcwd()
    script_content = f"""@echo off
cd /d "{current_dir}"
python run.py
pause
"""
    
    try:
        with open("start_jarvis.bat", "w", encoding="utf-8") as f:
            f.write(script_content)
        print("✅ start_jarvis.bat fayli yaratildi!")
        return True
    except Exception as e:
        print(f"❌ Skript yaratishda xato: {e}")
        return False

def main():
    """Asosiy setup funksiyasi"""
    print("🤖 Jarvis O'zbekcha Ovozli Yordamchi - Setup")
    print("=" * 50)
    
    # Tekshiruvlar
    if not check_python_version():
        return False
    
    check_os()
    
    # Paketlarni o'rnatish
    if not install_requirements():
        return False
    
    # Mikrofonni test qilish
    if not test_microphone():
        print("⚠️  Mikrofon muammosi bor, lekin davom etishingiz mumkin")
    
    # Startup skriptini yaratish
    create_startup_script()
    
    print("\n" + "=" * 50)
    print("🎉 Setup yakunlandi!")
    print("\n📋 Keyingi qadamlar:")
    print("1. 'python run.py' buyrug'ini ishga tushiring")
    print("2. Yoki 'start_jarvis.bat' faylini ikki marta bosing")
    print("3. 'Jarvis' deb chaqiring va buyruq bering")
    print("\n📖 Qo'shimcha ma'lumot uchun README.md va INSTALL.md fayllarini o'qing")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n❌ Setup bekor qilindi")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Kutilmagan xato: {e}")
        sys.exit(1)