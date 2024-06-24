import telebot
from telebot import types

bot = telebot.TeleBot('7232178964:AAHYKJvU_c2t15_RjFT6WOa78yLZ37ZDUaY')

ADMIN_CHANNEL_ID = '-1002147985788'

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

# Хранение состояния пользователя
user_states = {}

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data == 'information':
        bot.answer_callback_query(call.id)
        buttons_markup = create_buttons_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=buttons_markup)
    elif call.data == 'info_payment':
        bot.answer_callback_query(call.id)
        info_markup = create_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация про оплату.", reply_markup=info_markup)
    elif call.data == 'info_format':
        bot.answer_callback_query(call.id)
        info_markup = create_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация про формат обучения.", reply_markup=info_markup)
    elif call.data == 'info_schedule':
        bot.answer_callback_query(call.id)
        info_markup = create_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация про расписание.", reply_markup=info_markup)
    elif call.data == 'info_parents':
        bot.answer_callback_query(call.id)
        info_markup = create_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация для родителей.", reply_markup=info_markup)
    elif call.data == 'info_summer':
        bot.answer_callback_query(call.id)
        info_markup = create_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация про лето.", reply_markup=info_markup)
    elif call.data == 'feedback':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Пожалуйста, напишите свой вопрос для администрации:")
        user_states[call.message.chat.id] = 'awaiting_feedback'
    elif call.data == 'back':
        bot.answer_callback_query(call.id)
        buttons_markup = create_buttons_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=buttons_markup)

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'awaiting_feedback')
def handle_feedback(message):
    feedback_message = message.text
    user_id = message.chat.id
    user_info = message.from_user
    username = user_info.username
    if username:
        user_link = f"@{username}"
    else:
        user_link = f"[ID: {user_id}](tg://user?id={user_id})"
    bot.send_message(ADMIN_CHANNEL_ID, f"Пользователь {user_link} отправил сообщение: {feedback_message}", parse_mode='Markdown')
    bot.send_message(user_id, "Спасибо за ваш запрос! Мы свяжемся с вами в ближайшее время.")
    user_states.pop(user_id)


bot.polling(none_stop=True)