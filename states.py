from telebot.states import StatesGroup, State

class TranslatorState(StatesGroup):
    word = State()