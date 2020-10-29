"""STAFF infobot

Works on Sigur v2 library and Telebot (вылетает через несколько дней)

"""

from sigur import *
import telebot
import time

TOKEN = '1047143760:AAGB62SzV4J6l5rLzjspM6jr2EemeDDuYJQ'
CHAT = 183992731

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text.isdigit():
        person = Person(tab_no=int(message.text))
        person.init_data()
    else:
        person = Person()
        person.search_init(message.text)

    if person.initialized:
        bot.send_photo(CHAT, person.get_img_info())
    else:
        bot.send_message(CHAT, 'Person is not initialized')

while True:
    try:
        bot.polling(none_stop=True, timeout=150)
    except Exception as error:
        print(error)
        time.sleep(30)

