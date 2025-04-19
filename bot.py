import telebot
from telebot import apihelper

# ✅ توکن رباتت اینجاست
TOKEN = '5090610413:AAE3lZKpsOp6ps6uFsS_kQ0bCi0wdv4B-Qk'

# ✅ اینم پراکسی HTTP که قراره استفاده بشه
proxy = 'http://104.248.63.17:30588'  # ← اینو می‌تونی بعداً تغییر بدی

# ✅ تنظیم پراکسی توی کتابخونه
apihelper.proxy = {
    'http': proxy,
    'https': proxy
}

# ✅ ساخت بات
bot = telebot.TeleBot(TOKEN)

# ✅ جواب به دستور /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ ربات به درستی وصل شد!")

# ✅ اجرا
bot.polling()

