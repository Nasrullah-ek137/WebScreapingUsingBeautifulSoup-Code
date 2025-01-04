import requests
from bs4 import BeautifulSoup

url = "https://www.tutorialsfreak.com/"
web=requests.get(url)

soup= BeautifulSoup(web.content,"html.parser")

for i in soup.find_all("a"):
    print(i.get("href"))


# image information..

img=soup.find_all("img")

for ii in img:
    print(ii.get("src"))