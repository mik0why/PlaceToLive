import requests
from BeautifulSoup import BeautifulSoup
import csv

url = 'http://hdr.undp.org/en/composite/HDI'
response = requests.get(url) #headers not specified
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs = {"width" : 2268})

row_list = []
for row in table.findAll('tr'):
	cell_list = []
	for cell in row.findAll('td'):
#		txt = cell.text.replace('"', "") cos nie dziala
		txt = cell.text.encode('utf-8')
		cell_list.append(txt)
	row_list.append(cell_list)

outfile = open("./hdi.csv", "wb") #wb - opened by writing in binary mode
writer = csv.writer(outfile, delimiter = ';')
#writer.writerows("SEP=,")
writer.writerows(row_list)
reader = csv.reader(outfile)#, delimiter = ';')

#print table.prettify()