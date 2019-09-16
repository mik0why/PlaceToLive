# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import requests
import csv

url = 'https://tradingeconomics.com/country-list/personal-income-tax-rate'
response = requests.get(url)	

html = response.content
soup = BeautifulSoup(html)
table = soup.find('table', attrs = {"class": "table table-hover"})

row_list = []
i = 0
for row in table.findAll('tr'):
	cell_list = []
	if row.find('td') is not None: 
		country = row.find('a').contents[0]#.text#.encode('utf-8')
		value  = country.findNext('td').text#.encode('utf-8')
		print i, country
		#print i, country.find('a').contents[0], value
		if i>0: #not sure if necessary
			cell_list.append(i)
			cell_list.append(row.find('a').contents[0]) #before: .find('a').contents[0]) #encode text - for both of these
			cell_list.append(value)
		#there's a slight problem with Luxembourg but it shouldn't matter bc eventually it's all just gonna be uploaded to a larger table (for days off)
	i = i+1
	row_list.append(cell_list)


outfile = open("./taxes.csv", "wb")
writer = csv.writer(outfile, delimiter = ';')
writer.writerows(row_list)
reader = csv.reader(outfile)