import telebot
from telebot import types

bot = telebot.TeleBot('7232178964:AAHYKJvU_c2t15_RjFT6WOa78yLZ37ZDUaY')


def information_button():
    markup = types.InlineKeyboardMarkup()
    inf_button = types.InlineKeyboardButton('Узнать больше', callback_data='information')
    markup.add(inf_button)
    return markup


def create_buttons_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    # Создание всех 5 кнопок
    payment_info = types.InlineKeyboardButton("Про оплату", callback_data='info_payment')
    format_info = types.InlineKeyboardButton("Про обучение", callback_data='info_format')
    schedule_info = types.InlineKeyboardButton("Расписание", callback_data='info_schedule')
    parents_info = types.InlineKeyboardButton("Для родителей", callback_data='info_parents')
    summer_info = types.InlineKeyboardButton('Летнее обучение', callback_data='info_summer')
    # Добавление кнопок в markup
    markup.add(payment_info, format_info)
    markup.add(schedule_info, parents_info)
    markup.add(summer_info)
    return markup


def create_info_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    back_button = types.InlineKeyboardButton("Назад", callback_data='back')
    feedback_button = types.InlineKeyboardButton('Обратная связь', callback_data='feedback')
    markup.add(back_button, feedback_button)
    return markup


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '''👋 Привет! Я новый телеграм-бот 🤖. Моя цель — помочь вам найти необходимую информацию и ответить на все интересующие вас вопросы.

💡 Вот несколько вещей, которые я могу для вас сделать:

📚 Предоставить справочную информацию по интересующим вас темам.
❓ Ответить на ваши вопросы.
🖥️ Предоставить информацию о школе, ее услугах, процессах работы.

📋 Вот как вы можете взаимодействовать со мной:

🌟Воспользуйтесь кнопками предложенными снизу, в них вы можете найти необходимую для вас информацию.
Если вы не смогли найти нужную для вас информацию, вы можете связаться с администрацией.''', reply_markup=information_button())


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data == 'information':
        bot.answer_callback_query(call.id, "Вы нажали 'Узнать больше'")
        buttons_markup = create_buttons_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=buttons_markup)
    elif call.data == 'info_payment':
        bot.answer_callback_query(call.id, "Информация про оплату")
        info_markup = create_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация про оплату.", reply_markup=info_markup)
    elif call.data == 'info_format':
        bot.answer_callback_query(call.id, "Информация про формат обучения")
        info_markup = create_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация про формат обучения.", reply_markup=info_markup)
    elif call.data == 'info_schedule':
        bot.answer_callback_query(call.id, "Информация про расписание")
        info_markup = create_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация про расписание.", reply_markup=info_markup)
    elif call.data == 'info_parents':
        bot.answer_callback_query(call.id, "Информация для родителей")
        info_markup = create_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация для родителей.", reply_markup=info_markup)
    elif call.data == 'info_summer':
        bot.answer_callback_query(call.id, "Информация про лето")
        info_markup = create_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация про лето.", reply_markup=info_markup)
    elif call.data == 'feedback':
        bot.answer_callback_query(call.id, "Мы получили ваш запрос!")
        bot.send_message(call.message.chat.id, "Спасибо за ваш запрос! Мы свяжемся с вами в ближайшее время.")
    elif call.data == 'back':
        bot.answer_callback_query(call.id, "Возврат к выбору вариантов")
        buttons_markup = create_buttons_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=buttons_markup)

bot.polling(none_stop=True)