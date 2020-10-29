import pymysql.cursors
import smtplib
import time
import requests

hostname = '172.25.0.7'
TOKEN = '1235415463:AAFPeMTwBpXvy6KGPTFK-ti0nSaRHnn1WmA'

def send_telegram(mess: str):
    url = 'https://api.telegram.org/bot'+ TOKEN +'/sendMessage?chat_id=-465946296&text='
    req = url + mess
    requests.post(req)

def email_send_to_me(email_text):
    SUBJECT = "Test email from Python"
    TO = "doorwayder@gmail.com"
    FROM = "python.m@mail.ru"

    BODY = "\r\n".join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        email_text
    ))

    try:
        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.ehlo()
        server.login('python.m', 'Umbrella13')
        server.sendmail(FROM, TO, BODY.encode("utf8"))
        server.quit()
        print('Email OK')
    except Exception as ex:
        print('Email error')
        print(ex)
        return False

    return True


def get_person_zone(pid):
    connection = pymysql.connect(host=hostname,
                                 port=3305,
                                 user='root',
                                 password='spnx32_0',
                                 db='tc-db-main',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    # print("connect successful!!")

    try:

        with connection.cursor() as cursor:

            # SQL
            sql = "SELECT LOCATIONZONE FROM Personal WHERE Id = {}".format(pid)

            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)

    finally:
        # Закрыть соединение (Close connection).
        connection.close()

    return cursor.fetchone()['LOCATIONZONE']  # row['LOCATIONZONE']


def get_person_zone_name(pid):
    connection = pymysql.connect(host=hostname,
                                 port=3305,
                                 user='root',
                                 password='spnx32_0',
                                 db='tc-db-main',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:

        with connection.cursor() as cursor:

            # SQL
            sql = "SELECT LOCATIONZONE FROM Personal WHERE Id = {}".format(pid)

            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)

    finally:
        # Закрыть соединение (Close connection).
        connection.close()

    zone = cursor.fetchone()['LOCATIONZONE']
    if zone == 1:
        return 'внутренняя территория'
    else:
        return 'внешняя территория'


def get_person_name_by_id(pid):
    connection = pymysql.connect(host=hostname,
                                 port=3305,
                                 user='root',
                                 password='spnx32_0',
                                 db='tc-db-main',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:

        with connection.cursor() as cursor:

            # SQL
            sql = "SELECT NAME FROM Personal WHERE Id = {}".format(pid)
            cursor.execute(sql)


    finally:
        # Закрыть соединение (Close connection).
        connection.close()
    return cursor.fetchone()['NAME']


def get_person_id_by_name(name):
    connection = pymysql.connect(host=hostname,
                                 port=3305,
                                 user='root',
                                 password='spnx32_0',
                                 db='tc-db-main',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:

        with connection.cursor() as cursor:

            # SQL
            sql = 'SELECT Id FROM Personal WHERE NAME = "{}"'.format(name)
            # print(sql)
            cursor.execute(sql)


    finally:
        # Закрыть соединение (Close connection).
        connection.close()
    return cursor.fetchone()['Id']


def get_person_id_by_tab(tab):
    connection = pymysql.connect(host=hostname,
                                 port=3305,
                                 user='root',
                                 password='spnx32_0',
                                 db='tc-db-main',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:

        with connection.cursor() as cursor:

            sql = 'SELECT Id FROM Personal WHERE TABID = "{}"'.format(tab.zfill(10))
            cursor.execute(sql)


    finally:
        # Закрыть соединение (Close connection).
        connection.close()
    return cursor.fetchone()['Id']


def person_control_once(pid):
    person_zone = get_person_zone(pid)
    while True:
        if person_zone == get_person_zone(pid):
            time.sleep(5)
            continue
        else:
            print('{} - {}'.format(get_person_name_by_id(pid), get_person_zone(pid)))
            email_send_to_me('{} - {}'.format(get_person_name_by_id(pid), get_person_zone(pid)))
            break
    return True


def person_control(pid):
    person_zone = get_person_zone(pid)
    while True:
        if person_zone == get_person_zone(pid):
            time.sleep(5)
            continue
        else:
            print('{} - {}'.format(get_person_name_by_id(pid), get_person_zone(pid)))
            email_send_to_me('{} - {}'.format(get_person_name_by_id(pid), get_person_zone(pid)))
            person_zone = get_person_zone(pid)
    return True


def person_tele_control_once(id):
    person_zone = get_person_zone(id)
    while True:
        if person_zone == get_person_zone(id):
            time.sleep(5)
            continue
        else:
            print('{} - {}'.format(get_person_name_by_id(id), get_person_zone(id)))
            email_send_to_me('{} - {}'.format(get_person_name_by_id(id), get_person_zone(id)))
            break
    return True


# 183992731  CHAT ID
person_tab = '613'
mess = 'Start control...'
send_telegram(mess)

person_id = get_person_id_by_tab(person_tab)
person_zone = get_person_zone(person_id)
while True:
    if person_zone == get_person_zone(person_id):
        time.sleep(5)
        continue
    else:
        print('{} - {}'.format(get_person_name_by_id(person_id), get_person_zone_name(person_id)))
        if person_zone == 1:
            mess = 'Тигр вышел из клетки'
        else:
            mess = 'Медведь шатун в городе!!!'
        send_telegram(mess)
        person_zone = get_person_zone(person_id)
        # break
