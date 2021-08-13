from bs4 import BeautifulSoup
import requests

#Get horoscope from horoscope.com
def getHoroscope():
    r = requests.get("https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=4")
    soup = BeautifulSoup(r.content, 'html.parser')
    #Isolate paragraph to tweet
    a = soup.find('p')
    #Remove unecessary characters
    a = a.get_text()
    return a
