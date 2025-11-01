# Jarvis O'zgarishlar Tarixi

## [1.0.0] - 2024-11-01

### ✨ Yangi xususiyatlar
- 🎤 **Ovozli boshqaruv** - "Jarvis" hotword detection
- 🇺🇿 **To'liq o'zbekcha til** - Barcha javoblar o'zbekcha
- 🌐 **Ilovalar ochish** - YouTube, Google, Office va boshqalar
- 🎵 **YouTube musiqa** - Ovoz orqali qo'shiq ijro etish
- 💬 **Aqlli suhbat** - Tabiiy til bilan muloqot
- 🖥️ **Web interfeys** - Brauzer orqali boshqarish
- ⌨️ **Tezkor tugmalar** - Win+J tugmalari qo'llab-quvvatlash

### 🔧 Texnik xususiyatlar
- **Ovoz tanish**: Google Speech Recognition API
- **Ovoz sintezi**: pyttsx3 kutubxonasi
- **Web server**: Eel framework
- **Hotword detection**: SpeechRecognition kutubxonasi
- **Mikrofon sozlamalari**: Avtomatik mikrofon tanlash

### 📱 Qo'llab-quvvatlanadigan buyruqlar

#### Ilovalar ochish:
- "YouTube kir" - YouTube ochish
- "Kalkulyator kir" - Kalkulyator ochish
- "Bloknot kir" - Notepad ochish
- "Google kir" - Google ochish
- "Chrome kir" - Chrome brauzer ochish

#### YouTube musiqa:
- "YouTube da musiqa ijro et" - Umumiy musiqa
- "YouTube da [qo'shiq nomi] ijro et" - Aniq qo'shiq

#### Suhbat:
- "Salom" - Salomlashish
- "Qalaysiz" - Ahvol so'rash
- "Nima qila olasiz" - Imkoniyatlar ro'yxati
- "Soat necha" - Hozirgi vaqt
- "Yordam" - Yordam olish

### 🛠️ Texnik tafsilotlar
- **Python versiyasi**: 3.8+
- **OS qo'llab-quvvatlash**: Windows 10/11
- **Mikrofon**: Har qanday USB/built-in mikrofon
- **Internet**: Ovoz tanish uchun kerak

### 📦 Paketlar
- `speech_recognition` - Ovoz tanish
- `pyttsx3` - Ovoz sintezi  
- `eel` - Web interfeys
- `pyaudio` - Audio ishlov berish
- `pywhatkit` - YouTube integratsiya
- `requests` - HTTP so'rovlar
- `pygame` - Audio fayllar

### 🔒 Xavfsizlik
- Mahalliy ishlov berish - ma'lumotlar tashqariga chiqmaydi
- Ixtiyoriy yuz tanish - faqat mahalliy saqlanadi
- Ochiq manba kodi - barcha kod ko'rinadi

### 📋 Ma'lum muammolar
- Shovqinli muhitda ovoz tanish qiyinlashishi mumkin
- Ba'zi antiviruslar noto'g'ri signal berishi mumkin
- Birinchi ishga tushirishda sekinroq ishlashi mumkin

### 🔄 Keyingi versiyalar uchun rejalar
- [ ] Ko'proq tillar qo'llab-quvvatlash
- [ ] Mobil ilova versiyasi
- [ ] Uy aqlli qurilmalari bilan integratsiya
- [ ] Offline ovoz tanish
- [ ] Shaxsiy sozlamalar saqlash

---

## Versiya belgilash

Biz [Semantic Versioning](https://semver.org/) dan foydalanamiz:
- **MAJOR** - mos kelmaydigan o'zgarishlar
- **MINOR** - yangi xususiyatlar (orqaga mos)
- **PATCH** - xatolarni tuzatish

## Hissa qo'shish

O'zgarishlar tarixiga hissa qo'shish uchun:
1. Har bir o'zgarishni aniq tasvirlab yozing
2. Tegishli bo'limga joylashtiring
3. Sana va versiya raqamini qo'shing