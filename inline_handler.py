from telebot import types

def inline_handler(bot):
    @bot.inline_handler(func=lambda query: len(query.query) is 0)
    def query_text(query):
        hint = "Enter some number!"
        try:
            r = types.InlineQueryResultArticle(
                    id='1',
                    title="John bot",
                    description=hint,
                    input_message_content=types.InputTextMessageContent(
                    message_text="Calculating square")
            )
            bot.answer_inline_query(query.id, [r])
        except Exception as e:
             print(e)

    @bot.inline_handler(func=lambda query: len(query.query) > 0)
    def query_text(query):
        print(query)
        try:
            res = str(int(query.query) ** 2)
            r = types.InlineQueryResultArticle(
                    id='1', title="Square",
                    description="Result: {0}".format(res),
                    input_message_content=types.InputTextMessageContent(
                    message_text="Square of {0} is {1}".format(query.query, res))
            )
            bot.answer_inline_query(query.id, [r])
        except Exception as e:
             print(e)