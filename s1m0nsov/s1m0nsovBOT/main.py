import telebot
import logging
import os

from dotenv import load_dotenv

# callbacks
from callbacks.start_callback import StartCallbacks
from callbacks.menu_callback import MenuCallbacks

# handlers
from handlers.user_handlers import StartCommands

# Клавиатура
from keyboards import inline

load_dotenv()
token = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(token, parse_mode="HTML")

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


# import handlers 
start_commands_instance = StartCommands(bot)


# import callbacks 
start_callbacks_instance = StartCallbacks(bot)
menu_callbacks_instance = MenuCallbacks(bot)



# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
