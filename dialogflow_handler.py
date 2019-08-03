import apiai, json
import settings

def dialogflow_handler(bot):
    @bot.message_handler(content_types=['text'])
    def send_text(message):
        print('{id}: {text}'.format(id=message.from_user.first_name, text=message.text))

        request = apiai.ApiAI(settings.dialogflow).text_request()
        request.lang = 'ru'
        request.session_id = 'YarAIBot'
        request.query = message.text 
        responseJson = json.loads(request.getresponse().read().decode('utf-8'))
        response = responseJson['result']['fulfillment']['speech']
        
        bot.send_message(message.chat.id, response) if response else bot.send_message(message.chat.id, 'Dont understand')



