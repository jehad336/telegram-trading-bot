# استخدم نسخة Python 3.12 slim
FROM python:3.12-slim

# إنشاء مجلد للبوت داخل الحاوية
WORKDIR /app

# نسخ جميع ملفات البوت إلى داخل الحاوية
COPY . .

# تحديث pip وتثبيت المكتبات المطلوبة
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# الأمر لتشغيل البوت
CMD ["python", "bot.py"]
