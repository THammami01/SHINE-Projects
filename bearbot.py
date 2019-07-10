import requests
import json
import re
from random import randint
from time import sleep, strftime  # ctime, gmtime, localtime


def decor(func):
    def wrap(*args, **kwargs):
        print("---- START OF FUNC ----")
        func(*args, **kwargs)
        print("----- END OF FUNC -----")
    return wrap


class BearBot:
    def __init__(self):
        pass

    @decor
    def sendHearts(given_date=strftime("%c"), max_nbr_hearts=10, nbr_times=10, delay=1):
        """
        given_date: for example; Tue Jul  9 23:34:02 2019
        max_nbr_hearts: 10 hearts max per msg
        nbr_times: 10 msgs
        delay: 1 second
        """
        try:
            pending = True
            while pending:
                if (strftime("%c") == given_date):
                    for i in range(nbr_times):

                        heart = "❤️"
                        msg = ""
                        for i in range(randint(1, max_nbr_hearts)):
                            msg += heart

                        r = requests.get(
                            "https://api.telegram.org/bot848233233:AAFKYXkCxGgjZ6b32dPbkqE023uh1Ga-R94/sendMessage?chat_id=648853802&text=" + msg
                        )

                        sleep(delay)
                    pending = False
                    print("DONE")
                elif (strftime("%c") < given_date):
                    print("WAITING FOR: " + strftime("%c"))

                else:
                    pending = False
                    print("DEAD AT: " + given_date)
        except Exception as err:
            print(err)
            print("STOPED.")

    @decor
    def sendMsg(msg=None):
        try:
            r = requests.get(
                "https://api.telegram.org/bot848233233:AAFKYXkCxGgjZ6b32dPbkqE023uh1Ga-R94/sendMessage?chat_id=648853802&text=" + msg
            )
        except Exception as err:
            print(err)
            print("STOPED.")

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


# print(deleteSpaces(c))
# BearBot.sendMsg("Hiiiiiiiii !")
# BearBot.sendHearts(nbr_times=2)
# BearBot.getMe()
BearBot.pasteText()
