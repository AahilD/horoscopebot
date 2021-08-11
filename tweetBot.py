import tweepy
import logging
from config import createAPI
from tweetContent import getHoroscope
from bs4 import BeautifulSoup
import requests
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def tweetHoroscope(api, text):
    if len(text) > 280:
        listText = []
        shortText = ""
        i = 0
        for char in text:
            if i < 270:
                shortText += char
            if i >= 270:
                listText.append(shortText)
                shortText = ""
                i = -1
            i = i + 1
        listText.append(shortText)

        lenList = len(listText)
        j = 1
        for k in listText:
            k += (" %d/%d" % (j, lenList))
            j = j + 1
            api.update_status(k)




    if len(text) < 280:
        api.update_status(text)


def main():
    api = createAPI()
    horoscope = getHoroscope()
    while True:
        tweetHoroscope(api, horoscope)
        logger.info("Waiting...")
        time.sleep(86400)

if __name__ == "__main__":
    main()
