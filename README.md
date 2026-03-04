
<div align="center">

```
 ██████╗ ██████╗  ██████╗     ██████╗ ███╗   ███╗
██╔═══██╗██╔══██╗██╔════╝     ██╔══██╗████╗ ████║
██║   ██║██████╔╝██║  ███╗    ██║  ██║██╔████╔██║
██║   ██║██╔══██╗██║   ██║    ██║  ██║██║╚██╔╝██║
╚██████╔╝██████╔╝╚██████╔╝    ██████╔╝██║ ╚═╝ ██║
 ╚═════╝ ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝     ╚═╝
```

**ULTIMATE V2.0** — by **OBG STUDIO**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Discord](https://img.shields.io/badge/Discord-Bot-5865F2?style=for-the-badge&logo=discord)
![Platform](https://img.shields.io/badge/Platform-Termux-black?style=for-the-badge&logo=android)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 🇸🇦 عربي

### 📌 ما هي الأداة؟
**OBG DMBOT** أداة تيرمنال لإدارة رسائل Discord، تتيح لك:
- 💬 مراسلة أي شخص مباشرة عبر الـ DM
- 📢 إرسال رسائل جماعية لجميع أعضاء السيرفر
- 👁️ مراقبة وإرسال في قنوات النص

---

### ⚡ التثبيت والتشغيل

> افتح **Termux** وانسخ الأوامر بالترتيب:

```bash
pkg update && pkg upgrade -y
```
```bash
pkg install python git -y
```
```bash
pip install discord.py colorama
```
```bash
git clone https://github.com/Obadagamer/OBG-BOT-DM-.git
```
```bash
cd OBG-BOT-DM-
```
```bash
python 2.py
```

---

### 🔑 كيف أحصل على توكن البوت؟ (من الصفر)

**الخطوة 1 — افتح بوابة المطورين**
- اذهب إلى [discord.com/developers/applications](https://discord.com/developers/applications)
- سجّل الدخول بحسابك على Discord

**الخطوة 2 — أنشئ تطبيقاً جديداً**
- اضغط على زر **New Application** في الزاوية اليمنى العليا
- اكتب اسم البوت ثم اضغط **Create**

**الخطوة 3 — اذهب إلى قسم البوت**
- من القائمة اليسرى اضغط على **Bot**
- اضغط **Add Bot** ثم أكّد بـ **Yes, do it!**

**الخطوة 4 — فعّل الصلاحيات**
- تحت قسم **Privileged Gateway Intents** فعّل الثلاثة:
  - ✅ `PRESENCE INTENT`
  - ✅ `SERVER MEMBERS INTENT`
  - ✅ `MESSAGE CONTENT INTENT`
- اضغط **Save Changes**

**الخطوة 5 — انسخ التوكن**
- اضغط **Reset Token** ثم أكّد
- اضغط **Copy** وانسخ التوكن

**الخطوة 6 — أضف البوت للسيرفر**
- من القائمة اليسرى اضغط **OAuth2**
- اضغط على **OAuth2 URL Generator**
- انزل للأسفل وستجد قسم **Scopes** — ضع ✅ على **bot**
- بعدها سيظهر قسم **Bot Permissions** تحته — اختر الصلاحيات اللي تريدها
- انزل للأسفل وانسخ الرابط الظاهر في **Generated URL**
- افتح الرابط في المتصفح واختر السيرفر اللي تبي تضيف البوت فيه
- اضغط **Authorize** وأكمل التحقق

**الخطوة 7 — شغّل الأداة**
- الصق التوكن عند مطالبة الأداة به

> ⚠️ **تحذير:** لا تشارك توكن البوت مع أحد أبداً ولا ترفعه على GitHub

---

### 📋 المتطلبات
| المكتبة | الإصدار |
|---------|---------|
| `discord.py` | آخر إصدار |
| `colorama` | آخر إصدار |
| `python` | 3.8+ |

---

---

## 🌐 English

### 📌 What is this tool?
**OBG DMBOT** is a terminal-based Discord message manager that allows you to:
- 💬 Message anyone directly via DM
- 📢 Send mass messages to all server members
- 👁️ Monitor and send messages in text channels

---

### ⚡ Installation & Launch

> Open **Termux** and run these commands in order:

```bash
pkg update && pkg upgrade -y
```
```bash
pkg install python git -y
```
```bash
pip install discord.py colorama
```
```bash
git clone https://github.com/Obadagamer/OBG-BOT-DM-.git
```
```bash
cd OBG-BOT-DM-
```
```bash
python 2.py
```

---

### 🔑 How to get your Bot Token? (Step by Step)

**Step 1 — Open the Developer Portal**
- Go to [discord.com/developers/applications](https://discord.com/developers/applications)
- Log in with your Discord account

**Step 2 — Create a New Application**
- Click **New Application** in the top right corner
- Enter a name for your bot and click **Create**

**Step 3 — Go to the Bot Section**
- Click **Bot** from the left sidebar
- Click **Add Bot** then confirm with **Yes, do it!**

**Step 4 — Enable Privileged Intents**
- Under **Privileged Gateway Intents**, enable all three:
  - ✅ `PRESENCE INTENT`
  - ✅ `SERVER MEMBERS INTENT`
  - ✅ `MESSAGE CONTENT INTENT`
- Click **Save Changes**

**Step 5 — Copy the Token**
- Click **Reset Token** and confirm
- Click **Copy** to copy your bot token

**Step 6 — Add the Bot to your Server**
- From the left sidebar click **OAuth2**
- Click **OAuth2 URL Generator**
- Scroll down to the **Scopes** section — check ✅ **bot**
- A new section **Bot Permissions** will appear below — select the permissions you need
- Scroll down and copy the link shown in **Generated URL**
- Open the link in your browser and choose the server you want to add the bot to
- Click **Authorize** and complete the verification

**Step 7 — Run the Tool**
- Paste the token when the tool prompts you for it

> ⚠️ **Warning:** Never share your bot token with anyone or upload it to GitHub

---

### 📋 Requirements
| Library | Version |
|---------|---------|
| `discord.py` | Latest |
| `colorama` | Latest |
| `python` | 3.8+ |

---

<div align="center">

---

### 📲 تواصل معنا | Connect with us

[![TikTok](https://img.shields.io/badge/TikTok-@om0g0-ff0050?style=for-the-badge&logo=tiktok)](https://www.tiktok.com/@om0g0)
[![YouTube](https://img.shields.io/badge/YouTube-@obadagameing-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@obadagameing)
[![Discord](https://img.shields.io/badge/Discord-Server-5865F2?style=for-the-badge&logo=discord)](https://discord.gg/sxUGzPtv)

---

**© 2025 OBG STUDIO — All Rights Reserved**

*Made with ❤️ by OBG STUDIO*

</div>
