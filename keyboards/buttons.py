from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def dict_or_translate():
    markup = InlineKeyboardMarkup(keyboard=[
        [InlineKeyboardButton("Dictionary",callback_data="dictionary"),
         InlineKeyboardButton("Translate",callback_data="translate"),]
    ])
    return markup

def language_button():
    markup = InlineKeyboardMarkup()
    uz_tr = InlineKeyboardButton("🇺🇿 ➡️ 🇹🇷", callback_data="uz_tr")
    uz_en = InlineKeyboardButton("🇺🇿 ➡️ 🇬🇧", callback_data="uz_en")
    en_uz = InlineKeyboardButton("🇬🇧 ➡️ 🇺🇿", callback_data="en_uz")
    en_tr = InlineKeyboardButton("🇬🇧 ➡️ 🇹🇷", callback_data="en_tr")
    tr_uz = InlineKeyboardButton("🇹🇷 ➡️ 🇺🇿", callback_data="tr_uz")
    tr_en = InlineKeyboardButton("🇹🇷 ➡️ 🇬🇧", callback_data="tr_en")
    markup.add(uz_tr,uz_en,en_uz,en_tr,tr_uz,tr_en)
    return markup