from telebot import TeleBot
from os import environ

bot_token = str(environ.get('BOT_TOKEN'))
bot = TeleBot(bot_token)
