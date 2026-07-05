import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "✅ SMSBower Bot Online!\n\nস্বাগতম!"
    )

print("Bot Started...")
bot.infinity_polling(skip_pending=True)