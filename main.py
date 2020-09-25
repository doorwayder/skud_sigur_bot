from sigur import *
import telebot
import time

bot = telebot.TeleBot('701986116:AAGZ9sWRax4WjPw6fd6oo4MjmKKt7yVi7qQ')
# person = Person(tab_no=2359)
# person = Person(id_no=39)
# person = Person(person_name='Шалаев')

person = Person()
if person.search_init('Раскаткина'):
    print(person.name, person.id, person.tab)
    print(person.person_zone_name)
    print(person.person_zone_act)
    #bot.send_photo(183992731, person.get_img_info())
    person.get_img_info().show()

# for tab in range(9999):
#     person = Person(tab_no=tab)
#     if person.init_data():
#         photo = person.get_img_info()
#         if photo:
#             photo.show()
#         time.sleep(1)
