import telebot
import time
from telebot import apihelper
import schedule
import time
from telebot import types

bot = telebot.TeleBot('880475938:AAFZEAOKADR3YIIAa_Tggihlq6FPJVHi00E')  

apihelper.proxy = {'https': 'socks5://148.72.209.6:15681'}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'schedule is running!')
    #schedule.every().day.at('11:10').do(timer_alert, message)
    schedule.every(1).minutes.do(timer_alert, message)
    while True:
        schedule.run_pending()

@bot.message_handler(commands=['go'])
def go_message(message):
    bot.send_message(message.chat.id, 'Go from bot')

@bot.message_handler(commands=["geo"])
def geo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "ЕЕе! Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)

@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        print(message.location)
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))

@bot.message_handler(content_types=['text'])
def send_text(message):
    print('{id}: {text}'.format(id=message.from_user.first_name, text=message.text))
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id, 'Hi, John and Misha :-)')
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
