import requests
from BeautifulSoup import BeautifulSoup
import csv

#modify this - main should call one scraper and just specify which mode is needed
# if we're moving 1 td's next, or 4
# how to specify that argument?

#shouldn't actually it all be just one big scraper?

url = 'https://en.wikipedia.org/wiki/List_of_minimum_annual_leave_by_country'
response = requests.get(url) #headers not specified
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs = {"class" : "wikitable sortable"})

row_list = []
i = 0
for row in table.findAll('a'): #i guess this shouldn't be findAll bc it gets the annual leave and all this stuff as well
	i=i+1
	cell_list = []
	for cell in row:
		#temp = cell.findNext('td').text.encode('utf-8')
		#temp = soup.find('td', attrs = {"style" : "text-align:center;"}).findNext('td').findNext('td')

#		temp = soup.find('td').findNext('td').findNext('td').findNext('td')

		temp = cell.findNext('td').findNext('td').findNext('td').text.encode('utf-8')

		#temp = cell.findNext('td').findNext('td').findNext('td').findNext('td').text.encode('utf-8')
		#temp = temp.replace('&#8722;', '-')
		#print temp

		cell_list.append(i)
		cell_list.append(cell)
		cell_list.append(temp)
		print i, temp
		continue

	row_list.append(cell_list)


outfile = open("./days_off.csv", "wb")
writer = csv.writer(outfile, delimiter = ';')
writer.writerows(row_list)
reader = csv.reader(outfile)

#print table.prettify()