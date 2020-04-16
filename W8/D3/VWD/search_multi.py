import requests as r
from bs4 import BeautifulSoup as bs

def scrap(url):
    cont = bs(r.get(url).text,'html.parser')
    return cont.text
def count(text):
    z = input("Keyword?")
    count = 0
    cnt = text.split()
    for i in cnt:
        if z in i:
            count+=1
    print(count)
    return



def script():
    z = int(input("Press 1 to scrap hindu or 2 for times of india"))
    if z == 1:
        count(scrap("https://www.thehindu.com/"))
    else:

        count(scrap("https://timesofindia.indiatimes.com/"))
script()


