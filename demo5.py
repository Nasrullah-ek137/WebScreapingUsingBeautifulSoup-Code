from bs4 import BeautifulSoup
import requests

url = "https://www.tutorialsfreak.com/"
web = requests.get(url)
soup = BeautifulSoup(web.content, "html.parser")

#print(soup.prettify())

lines=soup.find_all("p")
for l in lines:
    print(l.text)

s=soup.find("h1",class_="main-heading my-3")
print(s)