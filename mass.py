"""WORKS WITH SIGUR library v.1 only"""

from sigur_lib import *
import time
import requests

TOKEN = '701986116:AAGZ9sWRax4WjPw6fd6oo4MjmKKt7yVi7qQ'

def send_telegram(mess: str):
    url = 'https://api.telegram.org/bot'+ TOKEN +'/sendMessage?chat_id=183992731&text='
    req = url + mess
    requests.post(req)

# 183992731  CHAT ID
persons_tab = ['1059',  # Шалаева
               '8205',  # Соколова
               '6986',  # Калашников
               '8594',  # Филипчук
               '7463',  # Квасницын
               '7902',  # Кочергин
               '2359',  # Мамулева
               '8485',  # Кузнецов
               '1566'  # Казаков
               ]

mess = "Start multi control"
send_telegram(mess)
persons_id = list()
for i, tab in enumerate(persons_tab):
    persons_id.append(get_person_id_by_tab(persons_tab[i]))

persons_zone = get_persons_zone(persons_id)
print(persons_zone)

while True:
    # new_persons_zone = copy.deepcopy(get_persons_zone(persons_id))
    new_persons_zone = get_persons_zone(persons_id)
    if persons_zone == new_persons_zone:
        time.sleep(10)
        continue
    else:
        persons_changed = compare_persons_list(persons_zone, new_persons_zone)
        for i in range(len(persons_changed)):
            if persons_changed[i]['LOCATIONZONE'] == 1:
                mess = get_person_name_by_id(persons_changed[i]['Id']) + '- внутр'
                send_telegram(mess)
            else:
                mess = get_person_name_by_id(persons_changed[i]['Id']) + '- внешн'
                send_telegram(mess)
        persons_zone = new_persons_zone
