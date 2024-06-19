import telebot
from telebot import types

bot = telebot.TeleBot('7232178964:AAHYKJvU_c2t15_RjFT6WOa78yLZ37ZDUaY')



def information_button():
    markup = types.InlineKeyboardMarkup()
    inf_button = types.InlineKeyboardButton('Узнать больше', callback_data='information')
    markup.add(inf_button)
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
    if call.message:
        if call.data == 'information':
            bot.send_message(call.message.chat.id, "общ информация")
    

bot.polling(none_stop=True)