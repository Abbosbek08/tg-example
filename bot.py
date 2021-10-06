import os
os.system("pip install pyTelegramBotApi")
import telebot
token="BOT TOKENI"
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
  user=message.chat.first_name
  text=f"Assalomu aleykum {user}"
  bot.reply_to(message,text)
bot.polling(none_stop=True)
