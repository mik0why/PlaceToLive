import requests
from BeautifulSoup import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature'
response = requests.get(url) #headers not specified
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs = {"class" : "wikitable sortable"})

row_list = []
i = 0
for row in table.findAll('a'):
	i=i+1
	cell_list = []
	for cell in row:
		temp = cell.findNext('td').text.encode('utf-8')
		temp = temp.replace('&#8722;', '-')
		cell_list.append(i)
		cell_list.append(cell)
		cell_list.append(temp)
	row_list.append(cell_list)


outfile = open("./weather.csv", "wb")
writer = csv.writer(outfile, delimiter = ';')
writer.writerows(row_list)
reader = csv.reader(outfile)

#print table.prettify()