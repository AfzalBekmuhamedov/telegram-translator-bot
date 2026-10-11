from telebot import TeleBot
from config import TOKEN
from database import DataBase
from telebot.custom_filters import StateFilter
from telebot.storage import StateMemoryStorage

db = DataBase()
bot = TeleBot(TOKEN, state_storage=StateMemoryStorage())
bot.add_custom_filter(custom_filter=StateFilter(bot))

