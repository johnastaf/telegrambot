from telebot import types
import datetime
import schedule
import settings

def schedule_handler(bot):
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'schedule is running!')
        #schedule.every().day.at('11:10').do(timer_alert, message)
        schedule.every(settings.delay_minutes).minutes.do(timer_alert, message, bot)
        while True:
            schedule.run_pending()

    @bot.message_handler(commands=['test'])
    def test_message(message):
         bot.send_message(message.chat.id, 'Test from BOT!')


def timer_alert(message, bot):
    print(datetime.datetime.now())
    bot.send_message(message.chat.id, 'schedule works!')
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    button_yes = types.KeyboardButton(text="/+")
    keyboard.add(button_yes)
    button_no = types.KeyboardButton(text="/-")
    keyboard.add(button_no)
    bot.send_message(message.chat.id, "Do you play today?", reply_markup=keyboard)
