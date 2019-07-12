import requests
import json
import re
from random import randint, choice
from time import sleep, strftime  # ctime, gmtime, localtime

chats = [
    {
        "name": "Me",
        "chat_id": 648853802
    },
    {
        "name": "Jhenifer",
        "chat_id": 741285841
    }
]


def decor(func):
    def wrap(*args, **kwargs):
        print(f"-- START OF {str(func)} --")
        func(*args, **kwargs)
        print(f"--- END OF {str(func)} ---")
    return wrap


class BearBot:
    def __init__(self):
        pass

    @decor
    def sendHearts(chat_id, given_date=strftime("%c"), max_nbr_hearts=8, nbr_times=10, delay=1):
        """
        given_date: for example; Tue Jul  9 23:34:02 2019
        max_nbr_hearts: 10 hearts max per msg
        nbr_times: 10 msgs
        delay: 1 second
        """
        pending = True
        while pending:
            if (strftime("%c") == given_date):
                for i in range(nbr_times):

                    msg = ""
                    for i in range(randint(1, max_nbr_hearts)):
                        heart = choice(
                            ["❤️", "❤️", "🧡", "💛", "💚", "💙", "💜", "🖤"]
                        )
                        msg += heart

                    r = requests.get(
                        "https://api.telegram.org/bot848233233:AAFKYXkCxGgjZ6b32dPbkqE023uh1Ga-R94/sendMessage?chat_id=" +
                        str(chat_id) + "&text=" + msg
                    )

                    sleep(delay)
                pending = False
            elif (strftime("%c") < given_date):
                print("WAITING FOR: " + strftime("%c"))
            else:
                pending = False
                print("DEAD AT: " + given_date)

    @decor
    def sendMsg(chat_id, msg):
        r = requests.get(
            "https://api.telegram.org/bot848233233:AAFKYXkCxGgjZ6b32dPbkqE023uh1Ga-R94/sendMessage?chat_id=" +
            str(chat_id) + "&text=" + msg
        )

    @decor
    def pasteText():
        r = requests.get(
            'https://1nine.com/Web/URLEncodeDecode'
        )
        file = open("Page.html", "w")
        file.write(r.text)
        file.close()

    @decor
    def getMe():
        r = requests.get(
            'https://api.telegram.org/bot848233233:AAFKYXkCxGgjZ6b32dPbkqE023uh1Ga-R94/getMe'
        )

        r = json.dumps(json.loads(r.text), indent=4)

        file = open("BearBot.json", "w")
        file.write(r)
        file.close()


chat_id = chats[0]["chat_id"]
msg = "❤️❤️ Have nice dreams ❤️❤️"
BearBot.sendMsg(chat_id, msg)

# BearBot.sendHearts(chat_id, max_nbr_hearts=8, nbr_times=10, delay=1)
