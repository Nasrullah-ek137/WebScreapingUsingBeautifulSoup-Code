from bs4 import BeautifulSoup
import requests

url = "http://www.google.com"
web = requests.get(url)
soup = BeautifulSoup(web.content, "html.parser")

#print(soup.prettify())

#print(soup.find_all("a"))

# BY CLASS ELEMENT
class_data=soup.find_all("div",class_="gb_J")
print(class_data)

id_data=soup.find_all("div",id="_2vvJZtSULcv41e8P7bzNqAU_8")
print(id_data)