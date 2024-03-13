from telebot import TeleBot, types

from keyboards import inline


class  StartCommands:
    def __init__(self, bot):
        self.bot = bot

    # Обработчик команды /start
        @bot.message_handler(commands=['start'])
        def handle_start(message):
            bot.send_message(message.chat.id, "Привет! Я бот помощник Артёма Симонсова\n"
                        "Тут ты сможешь найти все  конфиги/моды/рпшники Артема\n"
                        "Если у тебя не появилось меню то напиши /menu", reply_markup=inline.start)
            
        @bot.message_handler(commands=['menu'])
        def handle_menu(message):
            bot.send_message(message.chat.id, "<b>Вот твое меню</b>", reply_markup=inline.menu)
        
        
        # Обработчик текстовых сообщений
        @bot.message_handler(func=lambda message: True)
        def handle_text(message):
            bot.send_message(message.chat.id, "Прости, но я не понимаю обычный текст..\n"
                     "Если тебе нужна помощь то лучше напиши в лс Артёму -> @sads1m0nsov\n"
                     "Или воспользуйся меню")