from bs4 import BeautifulSoup as bs
import requests as req

base="http://www.fossbytes.com"

try:web_data=req.get(base)
except:print('a problem occured')
data=web_data.text
soup = bs(data,'lxml')

results=soup.find_all('h3')
for heading in results:
    print(f'> {heading.text}')