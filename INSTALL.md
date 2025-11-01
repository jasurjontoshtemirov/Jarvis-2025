# Jarvis O'rnatish Qo'llanmasi

Bu qo'llanma Jarvis ovozli yordamchini o'rnatish va sozlash bo'yicha batafsil ko'rsatmalar beradi.

## 📋 Tizim talablari

### Minimal talablar:
- **OS:** Windows 10/11
- **Python:** 3.8 yoki undan yuqori
- **RAM:** 4GB (tavsiya etiladi 8GB)
- **Disk:** 2GB bo'sh joy
- **Internet:** Ovoz tanish uchun

### Kerakli qurilmalar:
- **Mikrofon** - ovozli buyruqlar uchun
- **Dinamik/Quloqchin** - javoblarni eshitish uchun

## 🚀 Qadam-baqadam o'rnatish

### 1-qadam: Python o'rnatish

Agar Python o'rnatilmagan bo'lsa:

1. [python.org](https://python.org) saytiga kiring
2. "Download Python" tugmasini bosing
3. Yuklab olingan faylni ishga tushiring
4. **"Add Python to PATH"** ni belgilang
5. "Install Now" tugmasini bosing

Python o'rnatilganligini tekshirish:
```bash
python --version
```

### 2-qadam: Loyihani yuklab olish

#### Git orqali:
```bash
git clone https://github.com/[username]/Jarvis-2025.git
cd Jarvis-2025
```

#### ZIP fayl orqali:
1. GitHub sahifasida "Code" > "Download ZIP" tugmasini bosing
2. Faylni yuklab oling va arxivdan chiqaring
3. Papkaga kiring

### 3-qadam: Virtual muhit yaratish (tavsiya etiladi)

```bash
# Virtual muhit yaratish
python -m venv venv

# Virtual muhitni faollashtirish
# Windows CMD uchun:
venv\Scripts\activate

# Windows PowerShell uchun:
venv\Scripts\Activate.ps1

# Git Bash uchun:
source venv/Scripts/activate
```

### 4-qadam: Paketlarni o'rnatish

```bash
# pip ni yangilash
python -m pip install --upgrade pip

# Kerakli paketlarni o'rnatish
pip install -r requirements.txt
```

Agar xato yuz bersa:
```bash
pip install -r requirements.txt --force-reinstall --no-cache-dir
```

### 5-qadam: Mikrofonni sozlash

Mikrofonni tekshirish:
```bash
python test_microphone_fix.py
```

Bu sizga qaysi mikrofon ishlashini ko'rsatadi. Agar standart mikrofon ishlamasa, `backend/command.py` faylida o'zgartiring:

```python
# 47-qatorda:
with sr.Microphone(device_index=1) as source:  # 1 ni boshqa raqamga o'zgartiring
```

### 6-qadam: Jarvisni ishga tushirish

```bash
python run.py
```

Muvaffaqiyatli ishga tushsa:
- Konsol da "Jarvis ovozli yordamchi ishga tushdi" ko'rinadi
- Brauzer avtomatik ochiladi: `http://127.0.0.1:8000/index.html`

## 🔧 Sozlash

### Ovoz sozlamalari

`backend/command.py` faylida:
```python
# Ovoz sezgirligini o'zgartirish
r.energy_threshold = 300  # Pastroq qiymat = sezgirroq
r.pause_threshold = 0.8   # Pauza vaqti
```

### Ovoz tezligini o'zgartirish

`backend/command.py` faylida:
```python
# speak funksiyasida:
engine.setProperty('rate', 174)  # Tezlikni o'zgartiring (100-300)
```

## 🛠️ Muammolarni hal qilish

### Muammo 1: "ModuleNotFoundError"
**Yechim:**
```bash
pip install [paket_nomi]
# yoki
pip install -r requirements.txt --force-reinstall
```

### Muammo 2: Mikrofon ishlamaydi
**Yechim:**
1. Mikrofonni tekshiring: `python test_microphone_fix.py`
2. Boshqa mikrofon indeksini sinab ko'ring
3. Mikrofon ruxsatlarini tekshiring (Windows Settings > Privacy > Microphone)

### Muammo 3: "Permission denied" xatosi
**Yechim:**
```bash
# Administrator sifatida CMD/PowerShell ni oching
# yoki
pip install --user -r requirements.txt
```

### Muammo 4: Ovoz tanilmaydi
**Yechim:**
1. Internet aloqasini tekshiring
2. Mikrofonni yaqinroq qiling
3. Tinch muhitda gapiring
4. Aniq va sekin gapiring

### Muammo 5: YouTube ochilmaydi
**Yechim:**
1. Internet aloqasini tekshiring
2. Brauzer o'rnatilganligini tekshiring
3. Firewall sozlamalarini tekshiring

## 📱 Qo'shimcha sozlash

### Avtomatik ishga tushirish

Windows Startup papkasiga qo'shish:
1. `Win + R` tugmalarini bosing
2. `shell:startup` yozing va Enter bosing
3. Jarvis papkasiga shortcut yarating

### Tezkor tugmalar

`frontend/main.js` faylida tugmalarni o'zgartirish mumkin:
```javascript
// Win+J o'rniga boshqa tugma
if (e.key === "k" && e.metaKey) {  // Win+K
    // ...
}
```

## 🔄 Yangilash

Loyihani yangilash:
```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## 📞 Yordam

Agar muammolar davom etsa:
1. GitHub Issues bo'limida savol bering
2. README.md faylini qayta o'qing
3. Barcha qadamlarni qaytadan bajaring

## ✅ Tekshirish ro'yxati

- [ ] Python 3.8+ o'rnatilgan
- [ ] Git o'rnatilgan (ixtiyoriy)
- [ ] Loyiha yuklab olingan
- [ ] Virtual muhit yaratilgan va faollashtirilgan
- [ ] requirements.txt dan paketlar o'rnatilgan
- [ ] Mikrofon ishlaydi
- [ ] Internet aloqasi bor
- [ ] `python run.py` muvaffaqiyatli ishga tushdi
- [ ] Brauzer ochildi
- [ ] "Jarvis" deb chaqirish ishlaydi

Barcha belgilar ✅ bo'lsa, Jarvis tayyor!