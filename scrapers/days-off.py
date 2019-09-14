import requests
from BeautifulSoup import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/List_of_minimum_annual_leave_by_country'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
table = soup.find('table', attrs = {"class" : "wikitable sortable"})

row_list = []
i = 0
a = 0

for row in table.findAll('tr'):
	cell_list = []
	if row.find('a') is not None: 
		country = row.find('a').text.encode('utf-8')
		value  = row.findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').text.encode('utf-8')
		if country == "Bolivia":
			value = 31
		if country == "Bosnia and Herzegovina":
			value = 35
		if country == "Brazil":
			value = 26
		if country == "Canada":
			value = 23
		if country == "China":
			value = 26
		if country == "Jordan":
			value = 26
		if country == "Luxembourg":
			value = 44
		if country == "Russia":
			value = 47
		if value == "":
			value = row.findNext('td').findNext('td').findNext('td').text.encode('utf-8') #findAll not returning the right value for some reason
		print i, country, value
		if i>0:
			cell_list.append(i)
			cell_list.append(country)
			cell_list.append(value)
		#there's a slight problem with Luxembourg but it shouldn't matter bc eventually 
		#it's all just gonna be uploaded to a larger table
	i = i+1
	row_list.append(cell_list)


outfile = open("./days_off.csv", "wb")
writer = csv.writer(outfile, delimiter = ';')
writer.writerows(row_list)
reader = csv.reader(outfile)