from telebot import types
import schedule

def bot_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'schedule is running!')
        #schedule.every().day.at('11:10').do(timer_alert, message)
        schedule.every(1).minutes.do(timer_alert, message)
        while True:
            schedule.run_pending()

    @bot.message_handler(commands=['test'])
    def go_message(message):
         bot.send_message(message.chat.id, 'Test from BOT!')

    @bot.message_handler(commands=["geo"])
    def geo(message):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_geo = types.KeyboardButton(text="Send location", request_location=True)
        keyboard.add(button_geo)
        bot.send_message(message.chat.id, "Click the button and send you location", reply_markup=keyboard)

    @bot.message_handler(content_types=["location"])
    def location(message):
        if message.location is not None:
            print(message.location)
            print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))


def timer_alert(message):
    #nowTime = datetime.now()
    bot.send_message(message.chat.id, 'schedule works!')
    #print ('%s' % nowTime.strftime("%d.%m.%Y %H:%M:%S"), '// Send test timer message')
