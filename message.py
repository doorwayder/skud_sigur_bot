import requests


def send_telegram(token, chat, mess: str):
    req = 'https://api.telegram.org/bot'+ token +'/sendMessage?chat_id=' + chat + '&text=' + mess
    requests.post(req)
