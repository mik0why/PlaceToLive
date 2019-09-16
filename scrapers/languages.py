import requests
from BeautifulSoup import BeautifulSoup
import csv

url = 'https://www.infoplease.com/world/countries/languages-spoken-in-each-country-of-the-world'
response = requests.get(url) #headers not specified
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs = {"class" : "sgmltable"})

row_list = []
i = 0
for row in table.findAll('a'):
	i=i+1
	cell_list = []
	for cell in row:
		temp = cell.findNext('td').text.encode('utf-8')
		temp = temp.replace('&#8722;', '-')
		print i, cell,
		cell_list.append(i)
		cell_list.append(cell)
		cell_list.append(temp)
	row_list.append(cell_list)


outfile = open("./languages.csv", "wb")
writer = csv.writer(outfile, delimiter = ';')
writer.writerows(row_list)
reader = csv.reader(outfile)

#print table.prettify()