import telebot
from dialogflow import bot_text
from handlers import bot_handlers
import time
from telebot import apihelper
import time

bot = telebot.TeleBot('880475938:AAFZEAOKADR3YIIAa_Tggihlq6FPJVHi00E')

apihelper.proxy = {'https': 'socks5://163.172.81.30:443'}

bot_handlers(bot)
bot_text(bot)

while True:
    try:
        print('Starting...')
        bot.polling(none_stop=True, timeout=1000)
    except Exception as E:
        print(E)
        time.sleep(5)
