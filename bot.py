from sigur import *
import telebot
import time

bot = telebot.TeleBot('1397767064:AAEM9LElXOpDt9R9iLniEpdoRkEEmYHzBEM')


@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text.isdigit():
        person = Person(tab_no=int(message.text))
        person.init_data()
    else:
        person = Person()
        person.search_init(message.text)

    if person.initialized:
        bot.send_photo(183992731, person.get_img_info())
    else:
        bot.send_message(183992731, 'Person is not initialized')

while True:
    try:
        bot.polling(none_stop=True, timeout=150)
    except Exception as error:
        print(error)
        time.sleep(30)

