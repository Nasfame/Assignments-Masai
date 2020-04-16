import requests as r
from bs4 import BeautifulSoup as bs

blank = r.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
#print(blank) gives the status code

if blank.status_code==200:
    info = bs(blank.text,'html.parser')
    content = info.text
    print(content)
