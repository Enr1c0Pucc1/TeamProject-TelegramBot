import telebot
from telebot import types
from text import *

bot = telebot.TeleBot('7232178964:AAHYKJvU_c2t15_RjFT6WOa78yLZ37ZDUaY')

ADMIN_CHANNEL_ID = '-1002147985788'

user_states = {}

user_question = ''

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
    how_to_pay = types.InlineKeyboardButton("Как происходит оплата",callback_data="how_to_pay")
    education_info = types.InlineKeyboardButton("Как происходит обучение",callback_data="education_info")
    support_info = types.InlineKeyboardButton("Кураторская поддержка",callback_data="support_info")
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


def create_feedback_markup():
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("Назад", callback_data='back_to_menu')
    markup.add(back_button)
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
        pay_markup = create_pay_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация про оплату.", reply_markup=pay_markup)
    elif call.data == 'how_to_pay':
        bot.answer_callback_query(call.id)
        info_markup = create_pay_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Вы оплачиваете каждый период/абонемент (8 занятий по утвержденному расписанию), каждые 28 дней, в последний день предыдущего оплаченного периода. Мы будем об этом напоминать. Если нет возможности оплатить в срок предупредите, мы подождем, занятия при этом не приостанавливаем.
Новогодние, майские и летние каникулы исключение,
когда абонемент можно заморозить. В остальное время оплата идет каждые 8 занятий по расписанию.

Пропущенные основные занятия по любым причинам у вас не сгорают, а отрабатываются, вне расписания, по договоренности с педагогом, без привязке к оплате периодов. По запросу мы пришлем вам варианты, когда можно подключиться на отработку. Отработки проводятся в другой группе при наличии свободного места, либо индивидуально, но длительностью 45 минут. Если нет возможности отработать в учебное время, то копим пропуски и отрабатываем во время школьных каникул.

При покупке нескольких периодов предоставляем
скидки. Когда по вашей рекомендации к нам придет новый ученик - фиксированная скидка 2500 рублей на один период.

При решении сделать паузу в занятиях более трех недель без оплаты будущих уроков место в группе открепляется, и по возвращению если место занято - подбирается новая группа или педагог.""", reply_markup=info_markup)
    elif call.data == 'education_info':
            bot.answer_callback_query(call.id)
            info_markup = create_pay_info_markup()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Ребята от 9 до 17 обучаются в мини-группах до 4-х человек. С ними наставник-педагог.
    Программа состоит из модулей, в модулях лежат проекты, проекты поделены на шаги, в шаги вложена необходимая информация (статьи, ссылки, документация), необходимая к изучению для
    выполнения шага.

    По завершению проект отправляется на проверку. Проверяют действующие программисты и пишут ревью-код. После принятия открывается следующий проект модуля. Если пришли правки, то нужно доработать проект. Время проверки - от 3 до 24 часов. Пока проверяется проект одного модуля, выполняем проект другого модуля программы.

    Педагог будет помогать с возникшими вопросами, следить за происходящим, комментировать, объяснять при трудностях, курировать задачи.

    Материалы на платформе в доступен и вне занятий. Домашнее задание обычно - несколько шагов самостоятельно. От самостоятельной работы напрямую зависит скорость прогресса. Больше уделяет времени программированию - быстрее проходит программу. На урок можно подключаться уже с возникшими вопросами по задачам.""", reply_markup=info_markup)
    elif call.data == 'support_info':
            bot.answer_callback_query(call.id)
            info_markup = create_pay_info_markup()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Спасибо Вам, что выбрали нашу школу и доверили своего ребенка на обучение. Мы будем прикладывать все усилия, чтобы дать максимальный результат и добиться поставленных Вами целей

Что дальше?
Дальше у нас наступает первый месяц адаптации. Месяц, когда ученик знакомится ближе с педагогом, правилами группы, форматом обучения, своими обязанностями, и самое главное - начинает сталкиваться с первыми трудностями.	

Наша совместная задача, родителя и куратора - держать руку на пульсе и сразу реагировать на все замечания и комментарии ребенка на любые моменты
образовательного процесса. Это позволит понимать ситуацию и вносить изменения в работу, что снизит стресс у ребенка и поможет быстрее влиться в процесс.

Пишите пожалуйста, обратную связь и не бойтесь критиковать.
По всем вопросам - обращайтесь, с удовольствием
ответим.

Мы здесь на связи с Вами с 9 до 20 по Москве в будни и с 10 до 19 в выходные дни. Куратор при необходимости будет Вам звонить, обсуждать процесс обучения.

""", reply_markup=info_markup)
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
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Задайте вопрос к администратору.")
        user_states[call.message.chat.id] = 'awaiting_feedback'
    elif call.data == 'back_to_pay':
        bot.answer_callback_query(call.id)
        pay_markup = create_pay_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=pay_markup)
    elif call.data == 'back_to_summer':
        bot.answer_callback_query(call.id)
        summer_markup = create_summer_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=summer_markup)
    elif call.data == 'back_to_menu':
        bot.answer_callback_query(call.id)
        buttons_markup = create_buttons_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=buttons_markup)


@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'awaiting_feedback')
def handle_feedback(message):
    feedback_message = message.text
    user_id = message.chat.id
    feedback_markup = create_feedback_markup()
    global user_question
    if feedback_message.lower() == user_question.lower():
        bot.send_message(user_id, "Вы уже задавали этот вопрос.", reply_markup=feedback_markup)
    else:
        user_info = message.from_user
        username = user_info.username
        if username:
            user_link = f"@{username}"
        else:
            user_link = f"[ID: {user_id}](tg://user?id={user_id})"
        bot.send_message(ADMIN_CHANNEL_ID, f"Пользователь {user_link} отправил сообщение: {feedback_message}", parse_mode='Markdown')
        bot.send_message(user_id, "Спасибо за ваш запрос! Мы свяжемся с вами в ближайшее время.", reply_markup=feedback_markup)
        user_states.pop(user_id)
        user_question = feedback_message


bot.polling(none_stop=True)