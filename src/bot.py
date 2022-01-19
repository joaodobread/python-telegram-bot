from telebot import TeleBot
from telebot.types import Message, BotCommand
from src.config.environment import env


bot = TeleBot(env("TELEGRAM_TOKEN"))


class Bot:
    def __init__(self):
        bot.set_my_commands([
            BotCommand("help", "Some description")
        ])

    @bot.message_handler(commands=["help"])
    def asdf(message: Message):
        bot.reply_to(message, "Any Message")

    def start(self):
        bot.polling()
