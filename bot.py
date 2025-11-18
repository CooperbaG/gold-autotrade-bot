import telebot

TOKEN = "8599806981:AAG4TmmFxt6MnFInydTC41FCP1g76ACHYF0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Le bot fonctionne !")

bot.polling()
