import  requests as r
from bs4 import BeautifulSoup as bs
cont = bs(r.get("https://www.thehindu.com/").text, 'html.parser')
cont1 = bs(r.get("https://timesofindia.indiatimes.com/").text, 'html.parser')
with open('content.txt','w', encoding="utf-8") as f1:
    f1.write(cont.text)
    f1.write(cont1.text)

#cont1.encode('UTF-8')

## or u can string.encode(encoding='UTF-8',errors='strict')