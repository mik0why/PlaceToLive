#salary scraper
import requests
from BeautifulSoup import BeautifulSoup
import csv

# 1. the user needs to choose one profession from all the possibilities
# can be simply listed initially 
# 2. then need to scrape the number from all countries
#getting one entry from the list

#loc - country
#loctype - city
#job - job
#jobtype - not sure yet

url = 'https://www.numbeo.com/health-care/rankings_by_country.jsp'

i = 0
for i in range (243):
	url = 'http://www.salaryexplorer.com/salary-survey.php?loc=' + str(i) +'&loctype=1#disabled'
	#sth like that (with the i combined)
	response = requests.get(url) #headers not specified
	html = response.content

	soup = BeautifulSoup(html)
	table = soup.find('table', attrs = {"class" : "comparisonTable"})
	#if table is not None - not sure if that's the right way
	#entry = soup.find('td', string = "Administrative Assistant")
	if table is not None:
		print table.contents[0] #...sth like that

'''
row_list = []
val = 0
for row in table.findAll('tr'):
	print(str(val))
	cell_list = []
	cell_list.append(str(val))
	for cell in row.findAll('td'):
#		print("id found : ", cell.text ,"\n")
#		cell_list.append(val)
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
'''
