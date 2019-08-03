import telebot
from dialogflow_handler import dialogflow_handler
from vote_handler import vote_handler
from schedule_handler import schedule_handler
from inline_handler import inline_handler
from geo_handler import geo_handler
import time
from telebot import apihelper
import time
import settings

bot = telebot.TeleBot(settings.token)

apihelper.proxy = {'https': 'socks5://163.172.81.30:443'}

vote_handler(bot)
geo_handler(bot)
schedule_handler(bot)
dialogflow_handler(bot)
inline_handler(bot)

while True:
    try:
        print('Starting...')
        bot.polling(none_stop=True, timeout=1000)
    except Exception as E:
        print(E)
        time.sleep(5)
