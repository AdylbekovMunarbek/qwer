import telebot
import configure
from telebot import types 

client = telebot.Telebot(configure.config['6842447694:AAEf8sR7SiePk-3y-ceqb5XidSHJztfocRw'])


@client.message_handler (commands = ['get_info', 'info'])
def get_user_info(message):
    markur_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text = 'да', callback_data = 'yes')
    item_no = types.InlineKeyboardButton(text = 'нет', callback_data = 'no')

    markur_inline.add(item_yes, item_no)
    client.send_message(message.chat.id, 'Желаете узнать небольшую информатцию о вас',
        reply_markup = markur_inline
    )


@client.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('МОЙ ID')
        item_username = types.KeyboardButton('МОЙ НИК')

        markup_reply.add(item_id, item_username)
        client.send_message(call.message.chat.id, 'Нажмите на одну из кнопок',
           reply_markup = markup_reply
        )
    elif call.data == 'no':
        pass

@client.message_handler(content_types = ['text'])
def get_text(message):
    if message.text == 'МОЙ ID':
        client.send_message(message.chat.id, f'Your ID: {message.from_user.id}')
    elif message.text == 'МОЙ НИК':
        client.send_message(message.chat.id, f'Your ID: {message.from_user.first_name}  {message.from_user.last_name}')


client.polling(none_stop = True, interval = 0)





