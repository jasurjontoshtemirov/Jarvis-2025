# Jarvis - O'zbekcha Ovozli Yordamchi

Jarvis - bu o'zbekcha ovozli yordamchi dasturi bo'lib, u sizga turli vazifalarni bajarishda yordam beradi.

## 🎯 Imkoniyatlar

- 🎤 **Ovozli boshqaruv** - "Jarvis" deb chaqiring va buyruq bering
- 🌐 **Ilovalar ochish** - YouTube, Google, Kalkulyator va boshqalar
- 🎵 **YouTube musiqa** - Istalgan qo'shiqni YouTube da ijro eting
- 💬 **O'zbekcha suhbat** - To'liq o'zbekcha til qo'llab-quvvatlash
- 🖥️ **Web interfeys** - Brauzer orqali boshqarish

## 📋 Talablar

- Python 3.8 yoki undan yuqori
- Windows operatsion tizimi
- Mikrofon (ovozli buyruqlar uchun)
- Internet aloqasi

## 🚀 O'rnatish

### 1. Loyihani yuklab oling
```bash
git clone https://github.com/[sizning-username]/Jarvis-2025.git
cd Jarvis-2025
```

### 2. Virtual muhit yarating (tavsiya etiladi)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Kerakli paketlarni o'rnating
```bash
pip install -r requirements.txt
```

### 4. Jarvisni ishga tushiring
```bash
python run.py
```

## 🎤 Foydalanish

### Ovozli buyruqlar:
1. **"Jarvis"** deb ayting (hotword)
2. Buyruq bering:

**Ilovalar ochish:**
- "YouTube kir"
- "Kalkulyator kir" 
- "Bloknot kir"
- "Google kir"

**YouTube musiqa:**
- "YouTube da musiqa ijro et"
- "YouTube da [qo'shiq nomi] ijro et"

**Suhbat:**
- "Salom"
- "Qalaysiz"
- "Nima qila olasiz"
- "Soat necha"

### Web interfeys:
- Brauzer: `http://127.0.0.1:8000/index.html`
- Mikrofon tugmasini bosing yoki **Win+J** tugmalarini ishlating

## 🛠️ Sozlash

### Mikrofon muammolari:
Agar ovoz tanish ishlamasa, `backend/command.py` faylida mikrofonni o'zgartiring:
```python
with sr.Microphone(device_index=1) as source:  # 1 ni boshqa raqamga o'zgartiring
```

Mavjud mikrofonlarni ko'rish uchun:
```bash
python test_microphone_fix.py
```

## 📁 Loyiha tuzilishi

```
Jarvis-2025/
├── frontend/           # Web interfeys fayllari
├── backend/           # Python backend
│   ├── command.py     # Ovoz buyruqlari
│   ├── feature.py     # Asosiy funksiyalar
│   └── auth/          # Yuz tanish (ixtiyoriy)
├── run.py            # Asosiy ishga tushirish fayli
├── main.py           # Web server
└── requirements.txt  # Python paketlari
```

## 🎯 Qo'llab-quvvatlanadigan buyruqlar

### Ilovalar:
- YouTube, Google, Facebook, Instagram, Gmail
- Kalkulyator, Bloknot, Paint
- Chrome, Edge, Firefox
- Word, Excel, PowerPoint
- Telegram, WhatsApp, Skype

### Suhbat:
- Salomlashuvlar va xayrlashuvlar
- Vaqt va sana so'rash
- Yordam va imkoniyatlar haqida
- Umumiy suhbat

## 🔧 Muammolarni hal qilish

### Ovoz tanilmaydi:
1. Mikrofonni tekshiring
2. Internet aloqasini tekshiring
3. Boshqa mikrofon indeksini sinab ko'ring

### YouTube ochilmaydi:
1. Internet aloqasini tekshiring
2. Brauzer o'rnatilganligini tekshiring

### Paketlar o'rnatilmaydi:
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

## 🤝 Hissa qo'shish

1. Loyihani fork qiling
2. Yangi branch yarating (`git checkout -b yangi-xususiyat`)
3. O'zgarishlarni commit qiling (`git commit -am 'Yangi xususiyat qo'shildi'`)
4. Branch ni push qiling (`git push origin yangi-xususiyat`)
5. Pull Request yarating

## 📄 Litsenziya

MIT License - batafsil ma'lumot uchun [LICENSE](LICENSE) faylini ko'ring.

## 👨‍💻 Muallif

Jarvis O'zbekcha ovozli yordamchi

## 🙏 Minnatdorchilik

- OpenAI ChatGPT - AI yordami uchun
- Python jamoasi - ajoyib til uchun
- Barcha open source kutubxona mualliflari

---

**Eslatma:** Bu loyiha shaxsiy va ta'lim maqsadlarida yaratilgan. Tijorat maqsadlarida foydalanishdan oldin litsenziyani o'qing.