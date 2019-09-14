#healthcare scraper
import requests
from BeautifulSoup import BeautifulSoup
import csv

url = 'https://www.numbeo.com/health-care/rankings_by_country.jsp'
response = requests.get(url) #headers not specified
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs = {"id" : "t2"})

row_list = []
val = 0
for row in table.findAll('tr'):
	print(str(val))
	cell_list = []
	cell_list.append(str(val))
	for cell in row.findAll('td'):
		txt = cell.text.encode('utf-8')
		if txt != '':
			cell_list.append(txt)
	row_list.append(cell_list)
	val+=1

print(row_list)

outfile = open("./hqi.csv", "wb") #wb - opened by writing in binary mode
writer = csv.writer(outfile, delimiter = ';')
writer.writerows(row_list)
reader = csv.reader(outfile)#, delimiter = ';')
