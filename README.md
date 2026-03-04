# OBG STUDIO
عربي
# 🛡️ دليل تشغيل أداة OBG DMBOT على Termux

مرحباً بك في الأداة الأكثر تطوراً لإدارة حسابات ديسكورد عبر التيرموكس. تم تصميم هذه الأداة بواسطة OBG STUDIO لتوفير تجربة برمجية فاخرة وسريعة. اتبع الخطوات التالية بدقة لضمان التشغيل الصحيح:

1. تجهيز النظام الأساسي:
في البداية، نحتاج لتحديث كافة حزم النظام في تيرموكس لضمان عدم وجود توافقية ناقصة. قم بنسخ هذا الأمر:
$ pkg update && pkg upgrade -y

2. تثبيت لغة البرمجة وأدوات التحكم:
تعتمد الأداة بشكل أساسي على لغة Python ولتحميل الكود من الإنترنت نحتاج لأداة Git. قم بتثبيتهما معاً عبر هذا الأمر:
$ pkg install python git -y

3. تثبيت المكتبات البرمجية (المحركات):
الأداة تحتاج لمكتبات خارجية للتواصل مع "سيرفرات ديسكورد" وتلوين الواجهة البرمجية. قم بتثبيتها عبر مدير حزم بايثون:
$ pip install discord.py colorama

4. تحميل الأداة وتشغيلها:
الآن، سنقوم بجلب النسخة الأصلية من الأداة من مستودع Obadagamer وتشغيلها فوراً:
$ git clone https://github.com/Obadagamer/OBG-BOT-DM-.git
$ cd OBG-BOT-DM-
$ python 2.py



# English

# 🛡️ OBG DMBOT Operation Guide for Termux

Welcome to the most advanced Discord management tool for Termux. Developed by OBG STUDIO, this tool provides a premium, high-speed programming experience. Follow these steps carefully for a successful setup:

1. Initial System Preparation:
First, we must update all Termux system packages to ensure there are no compatibility issues. Copy and paste this command:
$ pkg update && pkg upgrade -y

2. Installing Programming Tools:
The tool runs primarily on Python. To download the code from GitHub, we need the Git tool. Install both using this command:
$ pkg install python git -y

3. Installing Software Libraries (Engines):
This tool requires external libraries to communicate with Discord servers and to style the terminal interface. Install them using the Python package manager:
$ pip install discord.py colorama

4. Cloning and Launching:
Now, we will fetch the original version of the tool from the Obadagamer repository and run it immediately:
$ git clone https://github.com/Obadagamer/OBG-BOT-DM-.git
$ cd OBG-BOT-DM-
$ python 2.py
