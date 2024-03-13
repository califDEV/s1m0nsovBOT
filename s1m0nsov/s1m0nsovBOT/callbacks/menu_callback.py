from telebot import TeleBot, types
from keyboards import inline

import os

class MenuCallbacks:
    def __init__(self, bot):
        self.bot = bot

        @bot.callback_query_handler(func=lambda call: call.data == 'mods')
        def open_menu_callback(call):
            self.bot.send_message(call.message.chat.id, "вот все моды которые я использую на 07.03.2024")
            mods_folder = 'file/mods'  # Путь к папке с файлами
    
            # Получение списка файлов в папке
            files = [f for f in os.listdir(mods_folder) if os.path.isfile(os.path.join(mods_folder, f))]
    
    # Проверка наличия файлов
            if not files:
                bot.send_message(call.message.chat.id, "Обратитесь к @californidze")
                return
    
    # Отправка файлов
            for file_name in files:
                file_path = os.path.join(mods_folder, file_name)
        
       
                with open(file_path, 'rb') as file:
                    bot.send_document(call.message.chat.id, file)
                    

        @bot.callback_query_handler(func=lambda call: call.data == 'resurspack')
        def open_menu_callback(call):
            self.bot.send_message(call.message.chat.id, "<b>Вот все мои РесурсПаки которые я использую на 07.03.2024 </b>\n")
            mods_folder = 'file/rp'  # Путь к папке с файлами
            
            files = [f for f in os.listdir(mods_folder) if os.path.isfile(os.path.join(mods_folder, f))]
            
            
            # Проверка наличия файлов
            if not files:
                bot.send_message(call.message.chat.id, "Обратитесь к @californidze")
                return
    
    # Отправка файлов
            for file_name in files:
                file_path = os.path.join(mods_folder, file_name)
        
       
                with open(file_path, 'rb') as file:
                    bot.send_document(call.message.chat.id, file)
        
        
        @bot.callback_query_handler(func=lambda call: call.data == 'settings')
        def open_menu_callback(call):
            self.bot.send_message(call.message.chat.id, "<b>Настройки Minecraft\n\n"
                                  "•fov - \"quick pro\"\n"
                                  "•Sensitivity - 70\n\n"
                                  "Так-же играю с LunarClient version 1.17.1 и Forge 1.16.5\n\n"
                                  "если вы тут что то не нашли то напиште @californidze, и чётко скажите что вас интересует"
                                  "</b>")
        
        
        
        @bot.callback_query_handler(func=lambda call: call.data == 'question')
        def open_menu_callback(call):
            self.bot.send_message(call.message.chat.id, 
                                  "<b>"
                                  "Привет! тут будут ответы на самые частые вопросы\n"
                                  "q - Вопрос, A - ответ\n\n"
                                  "q: С чего я играю? \nA: Играю я с LunarClient 1.17.1 или ForgeOptifine 1.16.5\n\n"
                                  "q:как сделать руки как у тебя? \nA:Я использую платный мод TopkaVisuals v2\n\n"
                                  "q:На каком сервере ты играешь?  \nA:HollyWorld Lite 1.16.5, Funtime\n\n"
                                  "q:А можно тебе денег скинуть? A: \nДа можно\n\n"
                                  "q:Как твое настроение?  \nA:сырок..\n\n"
                                  "q:Сколько тебе лет?  \nA: 17\n\n"
                                  "q:бля я уже не ебу какие ещё вопросы есть \nA:да..\n\n"
                                  "</b>")