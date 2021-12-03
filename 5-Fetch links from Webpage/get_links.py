# 检索网页中所有链接

import requests as rq
from bs4 import BeautifulSoup

url = input("输入网页链接:")
data = rq.get(url)
#print(data)

soup = BeautifulSoup(data.text,"html.parser")
#print(soup)

links = []

for link in soup.find_all("a"):
    links.append(link.get("href"))

#print(links)

with open("myLinks.txt", 'a') as saved:
    print(links[0:], file=saved)