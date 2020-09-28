# print("web scrapping")
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
links = soup.select('.storylink')[0]
votes = soup.select('.score')
print(soup.select('.storylink')[0])