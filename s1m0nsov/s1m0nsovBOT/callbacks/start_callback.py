from telebot import TeleBot
from keyboards import inline

class StartCallbacks:
    def __init__(self, bot):
        self.bot = bot

        @bot.callback_query_handler(func=lambda call: call.data == 'open_menu')
        def open_menu_callback(call):
            # Ваш код для обработки callback_data 'open_menu'
            self.bot.send_message(call.message.chat.id, "<b>Ваше меню:</b>",reply_markup=inline.menu)

        @bot.callback_query_handler(func=lambda call: call.data == 'send_contacts')
        def open_menu_callback(call):
            self.bot.send_message(call.message.chat.id, "<b>вот все  контакты:\n\nTG -> @sads1m0nsov\n"
                                  "TGK: @yokayyyy \n"
                                  "Нашли баг в боте? - @californidze </b>\n")