@echo off
echo ========================================
echo   Jarvis O'zbekcha Ovozli Yordamchi
echo ========================================
echo.

echo 1. Python versiyasini tekshirish...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python topilmadi! Iltimos Python 3.8+ o'rnating.
    pause
    exit /b 1
)

echo.
echo 2. Kerakli paketlarni o'rnatish...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ Paketlarni o'rnatishda xato!
    pause
    exit /b 1
)

echo.
echo 3. Jarvisni ishga tushirish...
echo ✅ Tayyor! Jarvis ishga tushmoqda...
echo.
echo 💡 Foydalanish:
echo    - "Jarvis" deb chaqiring
echo    - Buyruq bering: "YouTube kir", "Salom", va boshqalar
echo.

python run.py

pause