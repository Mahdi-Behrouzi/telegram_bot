import telebot

# توکن ربات که از BotFather گرفتی
TOKEN = '2137736951:AAFd_O8450uizaaf2wJDvv9qf0ZSic1mGec'
bot = telebot.TeleBot(TOKEN)

# هندلر برای فرمان /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! خوش اومدی به ربات تولیدی بهروزی 🎉")

# فعال نگه داشتن ربات
bot.infinity_polling()
