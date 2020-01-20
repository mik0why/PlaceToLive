from bs4 import BeautifulSoup
import requests

distance = 0
cc = {} #dictionary country, capital
#premise: for each country, compute the distance to the capital
#https://www.dystans.org/route.json?stops=Gdansk|NewYork


#cc["Germany"] ="Berlin"
#nah not adding manually, scrape from some website
#get 
#print(cc.get("Germany"))


def get_country_capital(table):
	url = "https://www.boldtuesday.com/pages/alphabetical-list-of-all-countries-and-capitals-shown-on-list-of-countries-poster"
	response = requests.get(url) #three crucial lines for BeautifulSoup to work
	html = response.content
	soup = BeautifulSoup(html, 'lxml')
	table = soup.find('table') #, attrs = {"class" : "youarehere"})
	rows = table.findAll('tr')

	for row in rows:
		entry = row.text.splitlines()
		country = entry[1].encode('utf-8').lower()
		capital = entry[2].encode('utf-8').lower()
		cc[country] = capital

get_country_capital(cc)


print cc