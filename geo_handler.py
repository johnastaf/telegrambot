from telebot import types

def geo_handler(bot):
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
