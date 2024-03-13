from telebot.util import quick_markup


start = quick_markup({
    'ᴍᴇɴᴜ💻': {'callback_data': 'open_menu'},
    'ᴄᴏɴᴛᴀᴄᴛs🔔': {'callback_data': 'send_contacts'},
}, row_width=2)


menu = quick_markup({
    'Моды ': {'callback_data': 'mods'},
    'РесурсПаки': {'callback_data': 'resurspack'},
    'Настройки ': {'callback_data': 'settings'},
    'Вопрос/Ответ': {'callback_data': 'question'},
}, row_width=2)