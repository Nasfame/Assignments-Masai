import requests as r
from bs4 import BeautifulSoup as bs

bk = r.get("https://timesofindia.indiatimes.com/")

cont = bs(bk.text,'html.parser')

print(cont.text)