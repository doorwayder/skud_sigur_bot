from sigur import *
import telebot

bot = telebot.TeleBot('701986116:AAGZ9sWRax4WjPw6fd6oo4MjmKKt7yVi7qQ')
#person = Person(tab_no=2359)
person = Person()
if person.search_init('Шалаева'):
    print(person.name, person.id, person.tab)
    print(person.person_zone_name)
    print(person.person_zone_act)
    bot.send_photo(183992731, person.get_img_info())
