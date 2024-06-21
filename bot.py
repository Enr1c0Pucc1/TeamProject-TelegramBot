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


def create_summer_info_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    back_button = types.InlineKeyboardButton("Назад", callback_data='back_to_summer')
    feedback_button = types.InlineKeyboardButton('Обратная связь', callback_data='feedback')
    markup.add(back_button, feedback_button)
    return markup


def create_summer_markup():
    #Добавление кнопкок для Лета
    markup = types.InlineKeyboardMarkup(row_width=2)
    available_activities = types.InlineKeyboardButton("Доступные активности", callback_data='activities_available')
    easy_summer = types.InlineKeyboardButton("Пакет «Лёгкое лето»", callback_data='summer_easy')
    active_time = types.InlineKeyboardButton("Пакет «Активное время»", callback_data='time_active')
    intensive_info = types.InlineKeyboardButton("Пакет «Интенсив»", callback_data='info_intensive')
    mentoring_info = types.InlineKeyboardButton("Пакет «Наставничество»", callback_data='info_mentoring')
    addition_info = types.InlineKeyboardButton("Допы от Клуба репетиторов", callback_data='info_addition')
     # Добавление кнопок в markup
    markup.add(available_activities)
    markup.add(easy_summer, active_time)
    markup.add(intensive_info, mentoring_info)
    markup.add(addition_info)
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
    previous_call = ''
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
        previous_call = 'info_summer'
        bot.answer_callback_query(call.id, previous_call)
        summer_markup = create_summer_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Информация про лето.", reply_markup=summer_markup)
        
    elif call.data == 'activities_available':
        bot.answer_callback_query(call.id, "Доступные активности")
        info_markup = create_summer_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Занятия с наставником
1 месяца / 8 занятий / 8 учебных часов

Занятия — онлайн-занятия в группе до 4-х учеников с наставником
по индивидуальной траектории обучения. С целью эффективного
изучения теории и её закрепления через создание проектов и
выполнение задач, поставленных на обучение.
                              
                              
                              
Хакатон
1 проект / 3 дней
 
Хакатон — ежемесячное онлайн-соревнование на 3 дня на котором, ребята
делают проекты от заказчика. За выполнение в срок получают призы и
сертификаты. С каждым участником персонально работает наставник.
                              
                              
                              
Клуб
1 месяц / 8 занятий / 16 учебных часа
 
Клуб — онлайн-встречи, на которых до 25 ребят встречаются 2 раза в
неделю по 2 часа, делают домашнюю работу, выполняют собственные
проекты, готовятся к соревнованиям и общаются на интересующие темы.
                              
                              
                              
Стажировка/Командный проект
10 дней / 20 учебных часов
                      
Ребята с желанием попробовать свои силы по пройденному материалу,
выполняют под руководством наставника до 5 проектов по ТЗ в течение 
2-х недель с понедельника по пятницу. Как результат резкий рост
мотивации к дальнейшему обучению.
                              
                              

Спецкурсы
Эксклюзивные мини-курсы, которые не находятся в открытом доступе
на платформе. набор на них производим 2 раза в год. Об актуальных
спецкурсах на лето уточните у куратора.""", reply_markup=info_markup)

    elif call.data == 'summer_easy':
        bot.answer_callback_query(call.id, "Легкое лето")
        info_markup = create_summer_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Для тех, кто хочет быстро пройти материал,
поучаствовать в стажировке и успеть отдохнуть
                              
Занятия с наставником
1 месяца / 8 занятий / 8 учебных часов
                              
Стажировка/Спецкурс
2 недели

Клуб
1 месяц / 8 занятий / 16 учебных часа
                              
2 Хакатона
2 проекта / 6 дней

                                      
В результате:
    1. Ученик применит полученные знания и повысит уверенность в своих силах
    2. Опыт участия в соревнованиях и в самостоятельной разработке
    3. Поднимется интерес и мотивация к обучению
    4. Пройдет программу на 20% быстрее и успеет отдохнуть летом
    5. С пользой проведет время, вместо YouTube и игр""", reply_markup=info_markup)
        
    elif call.data == 'time_active':
        bot.answer_callback_query(call.id, "Активное время")
        info_markup = create_summer_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Пакет «Активное время»
                              
Для тех, кто хочет заниматься круглый год и не пропустить занятия летом,
чтобы каникулы провести с пользой и участвовать в соревнованиях
                              
                              
Что входит в пакет?
                              
Стажировка/Спецкурс
2 недели
                              
3 Хакатона
3 проекта / 9 дней
                              
Клуб 
4 месяца / 32 занятий / 64 учебных часа
                              
Занятия с наставником
4 месяца / 32 занятий / 32 учебных часов

                              
В результате ваш ребёнок:
* Получит первый опыт разработки, который сверстники получат только на 2-м курсе ВУЗа
* Выполнит первые проекты по ТЗ в команде под руководством программиста
* Научится планировать свое время и организовывать процесс разработки
* Получит опыт участия в соревнованиях и в самостоятельной разработке
* Поднимет интерес и мотивацию к обучению на соревнованиях
* Применит полученные знания и повысит уверенность в ссвоих силах
* Пройдет программу на 20% быстрее, чем сверстники
* С пользой проведет время, вместо YouTube и игр 
* Найдет новых друзей с общими интересами
* Приблизится к оплачеваемой стажировке""", reply_markup=info_markup)
        
    elif call.data == 'info_intensive':
        bot.answer_callback_query(call.id, "Интенсив")
        info_markup = create_summer_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Пакет «Интенсив»
                              
Для ребят, кому нравится формат интенсивов и кто хочет
за лето пройти как можно больше программы и отдохнуть 
                              
                              
Что входит в пакет?
                              
Стажировка/Спецкурс
2 недели
                              
Клуб 
3 месяца / 24 занятий / 48 учебных часа
                              
3 Хакатона
3 проекта / 9 дней
                              
Занятия с наставником
2 месяца / 16 занятий / 16 учебных часов
                              
В результате ваш ребёнок:
* Получит первый опыт разработки, который сверстники получат только на 2-м курсе ВУЗа
* Выполнит первые проекты по ТЗ в команде под руководством программиста
* Научится планировать свое время и организовывать процесс разработки
* Получит опыт участия в соревнованиях и в самостоятельной разработке
* Поднимет интерес и мотивацию к обучению на соревнованиях
* Применит полученные знания и повысит уверенность в ссвоих силах
* Пройдет программу на 20% быстрее, чем сверстники
* С пользой проведет время, вместо YouTube и игр 
* Найдет новых друзей с общими интересами
* Приблизится к оплачеваемой стажировке""", reply_markup=info_markup)
        
    elif call.data == 'info_mentoring':
        bot.answer_callback_query(call.id, "Наставничество")
        info_markup = create_summer_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Пакет «Наставничество»
                              
Для ребят, которые хотят в 2-3 раза быстрее пройти
годовую программу и перейти на следующую ступень
                              
                              
Что входит в пакет?
                              
Наставничество
От 2 до 6 часов в неделю
Формат обучения при котором оплачивается стоимость за годовую
программу, а не за учебные часы. У ребенка неограниченное количество
занятий в месяц для максимально быстрого прохождения программы.
Например, пройти годовую программу вместе 9 месяцев за 3 месяца.
                       
3 Хакатона
3 проекта / 9 дней
                                                  
Занятия с наставником
Неограниченное количество
                              
В результате ваш ребёнок:
* Быстрее сверстников пройдет программу и перейдет на следующий год
* Быстрее получит результат и сэкономит время, а вы деньги
* Бесплатно участвует во всех активностях: хакатоны, клубы, и тд.""", reply_markup=info_markup)
        
    elif call.data == 'info_addition':
        bot.answer_callback_query(call.id, "Допы от Клуба репетиторов")
        info_markup = create_summer_info_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Допы от Клуба репетиторов

Кому нужно подтянуть школьную программу и разговорный
английский. У нас есть педагоги-партнеры по английскому
и математике. вы можете записаться к ним на занятия со
скидкой
                              
Доступные направления:
Английский
Математика
                              
В результате:
* Повышение успеваемости и уверености в школьных предметах.
* Практические навыки раговорного английского.
* Улучшение способности общаться на английском языке в повседневных ситуациях.
* Поднимется интерес и мотивация к обучению
* Пройдет программу на 20% быстрее, чем сверстники
* С пользой проведет время, вместо YouTube и игр""", reply_markup=info_markup)
        
    elif call.data == 'feedback':
        bot.answer_callback_query(call.id, "Мы получили ваш запрос!")
        bot.send_message(call.message.chat.id, "Спасибо за ваш запрос! Мы свяжемся с вами в ближайшее время.")

    elif call.data == 'back_to_summer':
        bot.answer_callback_query(call.id, "Возврат к выбору вариантов")
        summer_markup = create_summer_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=summer_markup)

    elif call.data == 'back':
        bot.answer_callback_query(call.id, "Возврат к выбору вариантов")
        buttons_markup = create_buttons_markup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Теперь выберите один из вариантов или свяжитесь с администрацией:", reply_markup=buttons_markup)

bot.polling(none_stop=True)