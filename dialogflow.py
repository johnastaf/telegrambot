import apiai, json

def bot_text(bot):
    @bot.message_handler(content_types=['text'])
    def send_text(message):
        print('{id}: {text}'.format(id=message.from_user.first_name, text=message.text))

        request = apiai.ApiAI('3725ca6c7af54fc0ac298fc295f9bc87').text_request()
        request.lang = 'ru'
        request.session_id = 'YarAIBot'
        request.query = message.text 
        responseJson = json.loads(request.getresponse().read().decode('utf-8'))
        response = responseJson['result']['fulfillment']['speech']
        if response:
            bot.send_message(message.chat.id, response)
        else:
            bot.send_message(message.chat.id, 'Dont understand')

        #if message.text.lower() == 'hi':
        #    bot.send_message(message.chat.id, 'Hi, John :-)')
        #elif message.text.lower() == 'bye':
        #    bot.send_message(message.chat.id, 'Bye, John')



