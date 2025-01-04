import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
web = requests.get('https://www.google.com')

# Parse the HTML content
soup = BeautifulSoup(web.content, 'html.parser')

# tag
tag=soup.p
print(tag)

tag2=soup.a
print(tag2)

# NavigableString
nav=soup.p.string
print(nav)

nav1=soup.a.string
print(nav1)


# BeautifulSoap

bs=soup.find('a')
print(bs)

'''
bs1=soup.find_all('a')
print(bs1)'''

