import os
import telebot

# Récupération du token depuis les variables d'environnement Render
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Le bot fonctionne !")

bot.polling()
