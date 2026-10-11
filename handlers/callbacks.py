from keyboards import dict_or_translate, language_button
from loader import bot, db
from telebot.types import CallbackQuery, Message
from translators.server import tss
from states import TranslatorState

@bot.callback_query_handler(func=lambda call:call.data in ['dictionary','translate'])
def dictionary_or_translate(call:CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id,call.message.id)
    if call.data == 'dictionary':
        result = db.select_table(chat_id)
        if len(result) > 0:
            text = "Lug'at"
            for key, value in result:
                text += f"{key} -> {value}"
        else:
            text = "Lug'at bo'sh!"
        bot.send_message(chat_id,text, reply_markup=dict_or_translate())
    else:
        bot.send_message(chat_id,"Tarjima", reply_markup=language_button())

@bot.callback_query_handler(func=lambda call:call.data in ['uz_tr','uz_en','en_uz','en_tr','tr_uz','tr_en'])
def translate_language(call:CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id,call.message.id)
    from_lang, to_lang = call.data.split("_")
    if from_lang == "uz":
        text = "So'z kiriting:"
    elif from_lang == "tr":
        text = "Kelime soyleyin"
    else:
        text = "Enter a word"
    bot.send_message(chat_id, text)
    bot.set_state(call.from_user.id,TranslatorState.word,chat_id)
    with bot.retrieve_data(user_id=call.from_user.id, chat_id=chat_id) as data:
        data['from_lang'] = from_lang
        data['to_lang'] = to_lang

@bot.message_handler(content_types=['text'], state=TranslatorState.word)
def translate_data(message:Message):
    chat_id = message.chat.id
    word = message.text
    with bot.retrieve_data(user_id=message.from_user.id,chat_id=chat_id) as data:
        from_lang = data['from_lang']
        to_lang = data['to_lang']
    translated_word = tss.google(word,from_lang,to_lang)
    with bot.retrieve_data(user_id=message.from_user.id,chat_id=chat_id) as data:
        data['word'] = word
        data['translated_word'] = translated_word
    bot.send_message(chat_id,translated_word)

