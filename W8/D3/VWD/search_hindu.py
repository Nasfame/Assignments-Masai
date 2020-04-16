import requests as r
from bs4 import BeautifulSoup as bs

bk = r.get("https://www.thehindu.com/")

cont = bs(bk.text,'html.parser')


if 'Covid' in cont.text:
    print("Yes")
