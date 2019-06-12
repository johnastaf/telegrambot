import telebot
import time
from telebot import apihelper

bot = telebot.TeleBot('880475938:AAFZEAOKADR3YIIAa_Tggihlq6FPJVHi00E')  

apihelper.proxy = {'https': 'socks5://50.195.104.171:1080'}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello from bot')


@bot.message_handler(commands=['go'])
def go_message(message):
    bot.send_message(message.chat.id, 'Go from bot')

while True:
    try:
        bot.polling(none_stop=True, timeout=200)
    except Exception as E:
        print(E.args)
        time.sleep(5)
