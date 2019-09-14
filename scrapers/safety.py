# -*- coding: utf-8 -*-
import requests
from BeautifulSoup import BeautifulSoup
import unicodecsv as csv
import sys

url = 'https://en.wikipedia.org/wiki/Global_Peace_Index#Global_Peace_Index_rankings_(2008–2019)'
url2 = "https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy"
url3 = "https://www.infoplease.com/world/countries/languages-spoken-in-each-country-of-the-world"
url4 = "https://en.wikipedia.org/wiki/List_of_countries_by_tax_rates"

# need some check here if sys.argv[1] is not null print sys.argv[1]
if sys.argv[1] == "h":
	website = url
elif sys.argv[1] == "l":
	website = url3 #lol organize this
elif sys.argv[1] == "t":
	website = url4
else:
	website = url2

response = requests.get(website)	

html = response.content
soup = BeautifulSoup(html)

if website == url3: #non wiki
	table = soup.find('table', attrs = {"class": "sgmltable"})
else:
	table = soup.find('table', attrs = {"class" : "wikitable sortable"})

#the whole tax part is gonna be annoying to edit

row_list = []
i = 0
a = 0

for row in table.findAll('tr'):
	cell_list = []
	if row.find('a') is not None: 
		country = row.find('a').text#.encode('utf-8')
		#if country == "CÃ´te d'Ivoire":
		#	print "!!!!"
		value  = row.findNext('td').findNext('td').text#.encode('utf-8')
		value = value.strip("=")
		print i, country, value
		#print i, country, value
		if i>0:
			cell_list.append(i)
			cell_list.append(country.encode('utf-8'))
			cell_list.append(value.encode('utf-8'))
		#there's a slight problem with Luxembourg but it shouldn't matter bc eventually it's all just gonna be uploaded to a larger table (for days off)
	i = i+1
	row_list.append(cell_list)

if sys.argv[1] == "h":
	outfile = open("./safety.csv", "wb")
elif sys.argv[1] == "l":
	outfile = open("./languages.csv", "wb")
elif sys.argv[1] == "t":
	outfile = open("./taxes.csv", "wb")
else:
	outfile = open("./life-exp.csv", "wb")
writer = csv.writer(outfile, delimiter = ';')
writer.writerows(row_list)
reader = csv.reader(outfile)