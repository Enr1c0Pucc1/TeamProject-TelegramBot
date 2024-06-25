import telebot
from telebot import types
from text import *

bot = telebot.TeleBot('7232178964:AAHYKJvU_c2t15_RjFT6WOa78yLZ37ZDUaY')


def information_button():
    markup = types.InlineKeyboardMarkup()
    inf_button = types.InlineKeyboardButton('Узнать больше', callback_data='information')
    markup.add(inf_button)
    return markup


def create_buttons_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    payment_info = types.InlineKeyboardButton("Про оплату", callback_data='info_payment')
    format_info = types.InlineKeyboardButton("Про обучение", callback_data='info_format')
    schedule_info = types.InlineKeyboardButton("Расписание", callback_data='info_schedule')
    parents_info = types.InlineKeyboardButton("Для родителей", callback_data='info_parents')
    summer_info = types.InlineKeyboardButton('Летнее обучение', callback_data='info_summer')
    markup.add(payment_info, format_info)
    markup.add(schedule_info, parents_info)
    markup.add(summer_info)
    return markup


def create_info_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    back_button = types.InlineKeyboardButton("Назад", callback_data='back_to_menu')
    feedback_button = types.InlineKeyboardButton('Обратная связь', callback_data='feedback')
    markup.add(back_button, feedback_button)
    return markup


def create_summer_info_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    back_button = types.InlineKeyboardButton("Назад", callback_data='back_to_summer')
    feedback_button = types.InlineKeyboardButton('Обратная связь', callback_data='feedback')
    markup.add(back_button, feedback_button)
    return markup


def create_summer_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    available_activities = types.InlineKeyboardButton("Доступные активности", callback_data='activities_available')
    easy_summer = types.InlineKeyboardButton("Пакет «Лёгкое лето»", callback_data='summer_easy')
    active_time = types.InlineKeyboardButton("Пакет «Активное время»", callback_data='time_active')
    intensive_info = types.InlineKeyboardButton("Пакет «Интенсив»", callback_data='info_intensive')
    mentoring_info = types.InlineKeyboardButton("Пакет «Наставничество»", callback_data='info_mentoring')
    addition_info = types.InlineKeyboardButton("Допы от Клуба репетиторов", callback_data='info_addition')
    back = types.InlineKeyboardButton("Назад", callback_data='back_to_menu')
    markup.add(available_activities)
    markup.add(easy_summer, active_time)
    markup.add(intensive_info, mentoring_info)
    markup.add(addition_info)
    markup.add(back)
    return markup


def create_pay_markup():
    markup=types.InlineKeyboardMarkup(row_width=2)
    how_to_pay = types.InlineKeyboardButton("Как происходит оплата", callback_data="how_to_pay")
    back = types.InlineKeyboardButton("Назад", callback_data='back_to_menu')
    markup.add(how_to_pay)
    markup.add(education_info)
    markup.add(support_info)
    markup.add(back)
    return markup


def create_pay_info_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    back_button = types.InlineKeyboardButton("Назад", callback_data='back_to_pay')
    feedback_button = types.InlineKeyboardButton('Обратная связь', callback_data='feedback')
    markup.add(back_button, feedback_button)
    return markup


def create_format_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    education_info = types.InlineKeyboardButton("Как происходит обучение", callback_data="education_info")
    support_info = types.InlineKeyboardButton("Кураторская поддержка", callback_data="support_info")
    back = types.InlineKeyboardButton("Назад", callback_data='back_to_menu')
    markup.add(education_info)
    markup.add(support_info)
    markup.add(back)
    return markup

def create_info_format_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    back_button = types.InlineKeyboardButton("Назад", callback_data='back_to_format')
    feedback_button = types.InlineKeyboardButton('Обратная связь', callback_data='feedback')
    markup.add(back_button, feedback_button)
    return markup


def create_parents_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    general_information = types.InlineKeyboardButton("Общая информация", callback_data="general_information")
    soft_skills_after_training = types.InlineKeyboardButton("Soft Skills после обучения", callback_data="soft_skills_after_training")
    hard_skills_after_training = types.InlineKeyboardButton("Hard skills после обучения", callback_data='hard_skills_after_training')
    back = types.InlineKeyboardButton("Назад", callback_data='back_to_menu')
    markup.add(general_information)
    markup.add(soft_skills_after_training)
    markup.add(hard_skills_after_training)
    markup.add(back)
    return markup

def create_info_parents_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    back_button = types.InlineKeyboardButton("Назад", callback_data='back_to_parents')
    feedback_button = types.InlineKeyboardButton('Обратная связь', callback_data='feedback')
    markup.add(back_button, feedback_button)
    return markup


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, start, reply_markup=information_button())


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data == 'information':
        bot.answer_callback_query(call.id)
        buttons_markup = create_buttons_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=buttons_markup)



    elif call.data == 'info_payment':
        bot.answer_callback_query(call.id)
        info_markup = create_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=how_to_pay, reply_markup=info_markup)



    elif call.data == 'info_format':
        bot.answer_callback_query(call.id)
        format_markup = create_format_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация про формат обучения.", reply_markup=format_markup)

    elif call.data == 'education_info':
        bot.answer_callback_query(call.id)
        info_markup = create_info_format_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=education_info, reply_markup=info_markup)

    elif call.data == 'support_info':
        bot.answer_callback_query(call.id)
        info_markup = create_info_format_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=support_info, reply_markup=info_markup)



    elif call.data == 'info_schedule':
        bot.answer_callback_query(call.id)
        info_markup = create_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация про расписание.", reply_markup=info_markup)



    elif call.data == 'info_parents':
        bot.answer_callback_query(call.id)
        parents_markup = create_parents_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация для родителей.", reply_markup=parents_markup)

    elif call.data == 'general_information':
        bot.answer_callback_query(call.id)
        info_markup = create_info_parents_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=general_information, reply_markup=info_markup)

    elif call.data == 'soft_skills_after_training':
        bot.answer_callback_query(call.id)
        info_markup = create_info_parents_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=soft_skills_after_training, reply_markup=info_markup)

    elif call.data == 'hard_skills_after_training':
        bot.answer_callback_query(call.id)
        info_markup = create_info_parents_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=hard_skills_after_training, reply_markup=info_markup)



    elif call.data == 'info_summer':
        bot.answer_callback_query(call.id)
        summer_markup = create_summer_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация про лето.", reply_markup=summer_markup)
        
    elif call.data == 'activities_available':
        bot.answer_callback_query(call.id)
        info_markup = create_summer_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=activities_available, reply_markup=info_markup)

    elif call.data == 'summer_easy':
        bot.answer_callback_query(call.id)
        info_markup = create_summer_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=summer_easy, reply_markup=info_markup)
        
    elif call.data == 'time_active':
        bot.answer_callback_query(call.id)
        info_markup = create_summer_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=time_active, reply_markup=info_markup)
        
    elif call.data == 'info_intensive':
        bot.answer_callback_query(call.id)
        info_markup = create_summer_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=info_intensive, reply_markup=info_markup)
        
    elif call.data == 'info_mentoring':
        bot.answer_callback_query(call.id)
        info_markup = create_summer_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=info_mentoring, reply_markup=info_markup)
        
    elif call.data == 'info_addition':
        bot.answer_callback_query(call.id)
        info_markup = create_summer_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=info_addition, reply_markup=info_markup)
        


    elif call.data == 'feedback':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Спасибо за ваш запрос! Мы свяжемся с вами в ближайшее время.")
    

    elif call.data == 'back_to_pay':
        bot.answer_callback_query(call.id)
        pay_markup = create_pay_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=pay_markup)


    elif call.data == 'back_to_summer':
        bot.answer_callback_query(call.id)
        summer_markup = create_summer_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=summer_markup)


    elif call.data == 'back_to_format':
        bot.answer_callback_query(call.id)
        format_markup = create_format_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=format_markup)


    elif call.data == 'back_to_parents':
        bot.answer_callback_query(call.id)
        parents_markup = create_parents_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=parents_markup)


    elif call.data == 'back_to_menu':
        bot.answer_callback_query(call.id)
        buttons_markup = create_buttons_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=buttons_markup)

bot.polling(none_stop=True)