import requests
import bs4
import lxml

res = requests.get('https://christhomas8.github.io')

soup = bs4.BeautifulSoup(res.text,'lxml')

title = soup.select('title')

print(title)

for link in soup.find_all('a',href=True):
	print(link['href'])
