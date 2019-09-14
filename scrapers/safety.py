# -*- coding: utf-8 -*-
import requests
from BeautifulSoup import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/Global_Peace_Index#Global_Peace_Index_rankings_(2008–2019)'
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
		country = row.find('a').text#.encode('utf-8')
		value  = row.findNext('td').findNext('td').text#.encode('utf-8')
		value = value.strip("=")
		print i, country, value
		if i>0:
			cell_list.append(i)
			cell_list.append(country)
			cell_list.append(value)
		#there's a slight problem with Luxembourg but it shouldn't matter bc eventually 
		#it's all just gonna be uploaded to a larger table
	i = i+1
	row_list.append(cell_list)


outfile = open("./safety.csv", "wb")
writer = csv.writer(outfile, delimiter = ';')
writer.writerows(row_list)
reader = csv.reader(outfile)