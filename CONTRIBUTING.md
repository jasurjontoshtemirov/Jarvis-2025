# Jarvis loyihasiga hissa qo'shish

Jarvis loyihasiga qiziqish bildirganingiz uchun rahmat! Bu qo'llanma sizga loyihaga qanday hissa qo'shishni ko'rsatadi.

## 🤝 Hissa qo'shish usullari

### 1. Xatolarni xabar qilish
- GitHub Issues bo'limida yangi issue yarating
- Xatoni batafsil tasvirlab yozing
- Qadamlar, kutilgan natija va haqiqiy natijani ko'rsating
- Tizim ma'lumotlarini qo'shing (OS, Python versiyasi)

### 2. Yangi xususiyat taklif qilish
- Avval Issues bo'limida muhokama qiling
- Xususiyatning foydasi va amalga oshirish usulini tushuntiring
- Jamoaning fikr-mulohazasini kuting

### 3. Kod yozish
- Fork yarating va yangi branch oching
- Kodni yozing va test qiling
- Pull Request yarating

## 🛠️ Rivojlantirish muhiti

### Kerakli dasturlar:
```bash
# Git
git --version

# Python 3.8+
python --version

# Code editor (VS Code tavsiya etiladi)
```

### Loyihani sozlash:
```bash
# Fork qilgan loyihani clone qiling
git clone https://github.com/[sizning-username]/Jarvis-2025.git
cd Jarvis-2025

# Virtual muhit yarating
python -m venv venv
venv\Scripts\activate

# Development paketlarini o'rnating
pip install -r requirements.txt
pip install -r requirements-dev.txt  # agar mavjud bo'lsa
```

## 📝 Kod yozish qoidalari

### Python kod uslubi:
```python
# PEP 8 standartiga amal qiling
# Funksiya nomlari: snake_case
def process_voice_command():
    pass

# Klass nomlari: PascalCase  
class VoiceRecognizer:
    pass

# Konstantalar: UPPER_CASE
MAX_RETRY_COUNT = 3

# O'zbekcha izohlar yozing
def salom_berish():
    """Foydalanuvchiga salom berish funksiyasi"""
    pass
```

### Fayl tuzilishi:
```
backend/
├── command.py      # Ovoz buyruqlari
├── feature.py      # Asosiy xususiyatlar  
├── config.py       # Sozlamalar
└── utils.py        # Yordamchi funksiyalar
```

### Commit xabarlari:
```bash
# Yaxshi commit xabarlari:
git commit -m "feat: YouTube qo'shiq ijro etish qo'shildi"
git commit -m "fix: mikrofon tanish muammosi hal qilindi"
git commit -m "docs: README fayli yangilandi"

# Commit turlari:
# feat: yangi xususiyat
# fix: xato tuzatish
# docs: hujjatlar
# style: kod formatlash
# refactor: kod qayta tuzish
# test: testlar
# chore: texnik ishlar
```

## 🧪 Test qilish

### Yangi kod yozishdan oldin:
```bash
# Mavjud testlarni ishga tushiring
python -m pytest tests/

# Yoki qo'lda test qiling
python test_voice_recognition.py
python test_youtube_commands.py
```

### Yangi testlar yozish:
```python
# tests/test_new_feature.py
def test_youtube_command():
    """YouTube buyrug'ini test qilish"""
    from backend.feature import PlayYoutube
    
    # Test ma'lumotlari
    query = "youtube da musiqa ijro et"
    
    # Funksiyani chaqirish
    result = PlayYoutube(query)
    
    # Natijani tekshirish
    assert result is not None
```

## 📋 Pull Request jarayoni

### 1. Branch yaratish:
```bash
git checkout -b yangi-xususiyat-nomi
```

### 2. O'zgarishlar qilish:
- Kodni yozing
- Testlar qo'shing
- Hujjatlarni yangilang

### 3. Commit qilish:
```bash
git add .
git commit -m "feat: yangi xususiyat qo'shildi"
```

### 4. Push qilish:
```bash
git push origin yangi-xususiyat-nomi
```

### 5. Pull Request yaratish:
- GitHub da "New Pull Request" tugmasini bosing
- O'zgarishlarni batafsil tasvirlab yozing
- Tegishli issue raqamini ko'rsating

### Pull Request shabloni:
```markdown
## O'zgarishlar tavsifi
Bu PR quyidagi o'zgarishlarni kiritadi:
- [ ] Yangi xususiyat qo'shildi
- [ ] Xato tuzatildi
- [ ] Hujjatlar yangilandi

## Test qilish
- [ ] Barcha mavjud testlar o'tdi
- [ ] Yangi testlar qo'shildi
- [ ] Qo'lda test qilindi

## Qo'shimcha ma'lumotlar
Issue #123 ni yechadi
```

## 🎯 Hissa qo'shish yo'nalishlari

### Yuqori ustuvorlik:
- [ ] Ovoz tanish sifatini yaxshilash
- [ ] Yangi o'zbekcha buyruqlar qo'shish
- [ ] Xatolarni tuzatish
- [ ] Hujjatlarni yaxshilash

### O'rta ustuvorlik:
- [ ] Yangi ilovalar qo'llab-quvvatlash
- [ ] Web interfeys yaxshilash
- [ ] Sozlamalar tizimi
- [ ] Loglar va monitoring

### Past ustuvorlik:
- [ ] Boshqa tillar qo'llab-quvvatlash
- [ ] Mobil versiya
- [ ] Plugin tizimi
- [ ] Grafik interfeys

## 📞 Aloqa

### Savollar:
- GitHub Issues orqali
- Email: [email manzili]
- Telegram: [telegram kanal]

### Muhokama:
- GitHub Discussions
- Discord server (agar mavjud bo'lsa)

## 🏆 Hissa qo'shuvchilar

Barcha hissa qo'shuvchilar README.md faylida e'tirof etiladi:

```markdown
## 👥 Hissa qo'shuvchilar

- [@username1](https://github.com/username1) - Asosiy rivojlantiruvchi
- [@username2](https://github.com/username2) - Ovoz tanish yaxshilash
- [@username3](https://github.com/username3) - Hujjatlar
```

## 📄 Litsenziya

Hissa qo'shish orqali siz o'z kodingizni MIT litsenziyasi ostida nashr etishga rozilik bildirasiz.

---

**Eslatma:** Birinchi marta hissa qo'shayotgan bo'lsangiz, kichik o'zgarishdan boshlang (masalan, hujjatlarni yaxshilash yoki kichik xatoni tuzatish).