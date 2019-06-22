import telebot
import time
from telebot import apihelper
import schedule
import time

bot = telebot.TeleBot('880475938:AAFZEAOKADR3YIIAa_Tggihlq6FPJVHi00E')  

apihelper.proxy = {'https': 'socks5://5.135.58.124:64980'}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'schedule is running!')
    #schedule.every().day.at('11-33').do(timer_alert, message)
    schedule.every().day.at("12:30").do(timer_alert, message)
    #schedule.every(1).minutes.do(timer_alert, message)
    while True:
        schedule.run_pending()

@bot.message_handler(commands=['go'])
def go_message(message):
    bot.send_message(message.chat.id, 'Go from bot')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id, 'Hi, John')
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'Bye, John')


def timer_alert(message):
    #nowTime = datetime.now()
    bot.send_message(message.chat.id, 'schedule works!')
    #print ('%s' % nowTime.strftime("%d.%m.%Y %H:%M:%S"), '// Send test timer message')


while True:
    try:
        print('Starting...')
        bot.polling(none_stop=True, timeout=1000)
    except Exception as E:
        print(E.args)
        time.sleep(5)
