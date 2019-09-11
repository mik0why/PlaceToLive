import requests
from BeautifulSoup import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature'
response = requests.get(url) #headers not specified
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs = {"class" : "wikitable sortable"})

row_list = []
for row in table.findAll('a'):
	cell_list = []
	for cell in row:
		cell_list.append(cell) #.encode('utf-8')?
	for new_cell in table.find('td'): #this just gives the country name
		cell_list.append(new_cell)	#and then operate on it in excel


		#now get the temperature as well


		#txt = cell.text.encode('utf-8')
		#cell_list.append(txt)
#		txt = cell.text.replace('"', "") cos nie dziala
	row_list.append(cell_list)

outfile = open("./weather.csv", "wb") #wb - opened by writing in binary mode
writer = csv.writer(outfile, delimiter = ';')
#writer.writerows("SEP=,")
writer.writerows(row_list)
reader = csv.reader(outfile)#, delimiter = ';')

#print table.prettify()