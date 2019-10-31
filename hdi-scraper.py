import requests
from BeautifulSoup import BeautifulSoup
import csv
import pandas as pd

url = 'http://hdr.undp.org/en/composite/HDI'
response = requests.get(url) #headers not specified
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs = {"width" : 2268})

row_list = []
for row in table.findAll('tr'):
	cell_list = []
	for cell in row.findAll('td'):
		txt = cell.text.encode('utf-8')
		cell_list.append(txt)
	row_list.append(cell_list)

outfile = open("./hdi.csv", "wb") #wb - opened by writing in binary mode
writer = csv.writer(outfile, delimiter = ';')
writer.writerows(row_list)
reader = csv.reader(outfile)#, delimiter = ';')

# has to be done differently bc it's in a different format than salary.csv ?
df = pd.read_csv("./hqi.csv", header = None, error_bad_lines = False,  delimiter=';')
df.rename(columns = {0: 'idx', 1: 'Country', 2: 'Val1', 3: 'Val2'}, inplace = True)
df.sort_values(by = 'Val1', inplace = True, ascending = False)

# the last thing - reset values of 'idx'
df.to_excel("sorted_hqi.xlsx", index = False) #should it have the prof in the name?





#print table.prettify()