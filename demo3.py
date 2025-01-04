import requests
from bs4 import BeautifulSoup

url="https://www.amazon.com/"

web=requests.get(url)

soup= BeautifulSoup(web.text,"lxml")

bsss=soup.find_all("a")
print(bsss)