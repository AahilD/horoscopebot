#Import required packages
from bs4 import BeautifulSoup
import requests

def getHoroscope():
    #Read URL and enter it into HTML parser
    r = requests.get("https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=4")
    soup = BeautifulSoup(r.content, 'html.parser')
    #Isolate paragraph to tweet
    a = soup.find('p')
    #Edit paragraph
    a = a.get_text()
    return a
