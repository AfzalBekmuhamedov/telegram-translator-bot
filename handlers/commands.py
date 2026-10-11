from telebot.types import Message
from keyboards import dict_or_translate
from loader import bot


@bot.message_handler(commands=['start','help'])
def commands(message:Message):
    chat_id = message.chat.id
    if message.text == '/start':
        bot.send_message(chat_id,f"Salom {message.from_user.full_name}",reply_markup=dict_or_translate())
    else:
        bot.send_message(chat_id,"What kind of help you need?")