import requests as r
from bs4 import BeautifulSoup as bs

blank = r.get("https://www.facebook.com/")
#print(blank) gives the status code
print(blank.text)
if blank.status_code==200:
    info = bs(blank.text,'html.parser')
    content = info.text
    print(content)
