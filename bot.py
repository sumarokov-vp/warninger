from telebot import TeleBot
from settings import get_setting

bot = TeleBot(get_setting('bot_token'))
