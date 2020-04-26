from bs4 import BeautifulSoup
import requests

HOST = 'https://t24.com.tr'
PATH = '/yazarlar/'

AUTHORS = ['murat-belge', 'mehmet-y-yilmaz']

source = requests.get(HOST + PATH + AUTHORS[1]).text

soup = BeautifulSoup(source, 'lxml')

articles = soup.find_all('div', class_='_1fE_V')

for article in articles:
	date = article.find('div', class_='_2J9OF col-sm-3 col-xs-12').p.next_sibling.text
	headline = article.find('div', class_='_31Tbh col-sm-9 col-xs-12').h3.a.text
	link = article.find('div', class_='_31Tbh col-sm-9 col-xs-12').h3.a['href']
	
	articlePage = requests.get(HOST + link).text
	soup2 = BeautifulSoup(articlePage, 'lxml')
	body = soup2.find('div', class_='_2teaB')
	
	try:
		h2 = body.h2
	except Exception as e:
		h2 = None	
	
	try:
		mainBody = h2.find_next('div').div
	except Exception as e:
		mainBody = body.find('div', class_='_1NMxy').div
	
	print(h2)
	print(mainBody)
	# print(date)
	# print(headline)
	# print(link)
	print()