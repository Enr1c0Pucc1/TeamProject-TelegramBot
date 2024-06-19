import telebot
from telebot import types

bot = telebot.TeleBot('7232178964:AAHYKJvU_c2t15_RjFT6WOa78yLZ37ZDUaY')


def feedback_button():
    markup = types.InlineKeyboardMarkup()
    feedback_button = types.InlineKeyboardButton('Связаться с администрацией', callback_data='feedback')
    markup.add(feedback_button)
    return markup


@bot.message_handler(commands=['start'])
def main(message):
    feedback_markup = feedback_button()
    bot.send_message(message.chat.id, '''👋 Привет! Я новый телеграм-бот 🤖. Моя цель — помочь вам найти необходимую информацию и ответить на все интересующие вас вопросы.

💡 Вот несколько вещей, которые я могу для вас сделать:

📚 Предоставить справочную информацию по интересующим вас темам.
❓ Ответить на ваши вопросы.
🖥️ Предоставить информацию о школе, ее услугах, процессах работы.

📋 Вот как вы можете взаимодействовать со мной:

🌟Воспользуйтесь кнопками предложенными снизу, в них вы можете найти необходимую для вас информацию.
Если вы не смогли найти нужную для вас информацию, вы можете связаться с администрацией.''', reply_markup=feedback_markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        bot.answer_callback_query(call.id, "Мы получили ваш запрос!")
        bot.send_message(call.message.chat.id, "Спасибо за ваш запрос! Мы свяжемся с вами в ближайшее время.")


bot.polling(none_stop=True)