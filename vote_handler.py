import settings

users = {}

def vote_handler(bot):
    @bot.message_handler(commands=['+'])
    def plus_message(message):
        if not message.from_user.is_bot and not message.from_user.id in users.keys():
            users[message.from_user.id] = message.from_user.first_name;
            bot.send_message(message.chat.id, '+1')

    @bot.message_handler(commands=['-'])
    def minus_message(message):
         if not message.from_user.is_bot and message.from_user.id in users.keys():
             del users[message.from_user.id]
             bot.send_message(message.chat.id, '-1')

    @bot.message_handler(commands=['info'])
    def minus_message(message):
         bot.send_message(message.chat.id, 'Users: {count}'.format(count=len(users)))
         bot.send_message(message.chat.id, 'Who: {who}'.format(who=' '.join(users.values())))
