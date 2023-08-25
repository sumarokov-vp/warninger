from telebot import TeleBot
from os import environ

bot_token = str(environ.get('BOT_TOKEN'))
if not bot_token:
    raise Exception("BOT_TOKEN env variable is not set")
if bot_token =='':
    raise Exception("BOT_TOKEN env variable is empty")
if bot_token == 'None':
    raise Exception("BOT_TOKEN env variable is None\nUse export BOT_TOKEN=\"your_token\"")

print(f"Bot token: {bot_token}")
bot = TeleBot(bot_token)
