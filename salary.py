#-*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import requests
import csv


def wage_scrape(job_type):
	jobs = {
		1: "Information Technology",
		2: "Health and Medical",
		3: "Import and Export",
		4: "Accounting and Finance",
		5: "Fundraising and Non Profit",
		6: "Administration / Reception / Secretarial",
		7: "Advertising / Grapic Design / Events",
		8: "Airlines / Aviation / Aerospace / Defense",
		9: "Architecture",
		10: "Automotive",
		11: "Bilingual",
		12: "Independent Jobs",
		13: "Banking",
		14: "Business Planning",
		15: "Care Giving and Child Care",
		16: "Cleaning and Housekeeping",
		17: "Construction / Building / Installation",
		18: "Counseling",
		19: "Customer Service and Call Center",
		20: "Courier / Delivery / Transport / Drivers",
		21: "Electrical and Electronics Trades",
		22: "Engineering",
		23: "Environmental",
		24: "Executive and Management",
		25: "Fashion and Apparel",
		26: "Facilities / Maintenance / Repair",
		27: "Fitness / Hair / Beauty",
		28: "Food /Hospitality / Tourism / Catering",
		29: "Gardening / Farming / Fishing",
		30: "Government and Defence",
		31: "Human Resources",
		32: "Insurance",
		33: "Factory and Manufacturing",
		34: "Law Enforcement / Security / Fire",
		35: "Legal",
		36: "Marketing",
		37: "Pet Care",
		38: "Media / Broadcasting / Arts / Entertainment",
		39: "Oil / Gas / Energy / Mining",
		40: "Photography",
		41: "Pharmaceutical and Biotechnology",
		42: "Public Relations",
		43: "Publishing and Printing",
		44: "Quality Control and Compliance",
		45: "Purchasing and Inventory",
		46: "Real Estate",
		47: "Recreation and Sports",
		48: "Sales Retail and Wholesale",
		49: "Science and Technical Services",
		50: "Teaching / Education",
		51: "Telecommunication"
	}

	#then can add more specific job to each subcategory? 
	#annoying to implement but a useful functionality

	for item in jobs.keys():
		if jobs[item] == job_type:
			return item


	scrape_to_csv(value) #ok for now but later will be modified

#wage_scrape("Marketing")

#now import all the salaries from around the world to the doc


def scrape_to_csv(idx):
	for i in range(244):
		url = "http://www.salaryexplorer.com/salary-survey.php?loc=" + str(i) + "&loctype=1&job=" + str(idx) + "&jobtype=1"
		print url
# loc needs to iterate
#job is obtained from 


#scrape_to_csv(40)


'''
url = 'https://tradingeconomics.com/country-list/personal-income-tax-rate'
response = requests.get(url)	

html = response.content
soup = BeautifulSoup(html)
table = soup.find('table', attrs = {"class": "table table-hover"})

row_list = []
i = 0
for row in table.findAll('tr'):
	cell_list = []
	if row.find('td') is not None: 
		country = row.findAll('a')[0].contents[0].string	# if this doesn't work then just add the "string" part separately
		value  = country.findNext('td').text.encode('utf-8') # just for now
		country = country.string.replace('\r\n', '').encode('utf-8').strip()#[0].contents
#		print i, country
		if i>0: #not sure if necessary
			cell_list.append(i)
			cell_list.append(country) #before: .find('a').contents[0]) #encode text - for both of these
			cell_list.append(value) #just for now
			print cell_list
		#there's a slight problem with Luxembourg but it shouldn't matter bc eventually it's all just gonna be uploaded to a larger table (for days off)
	i = i+1
	row_list.append(cell_list)


outfile = open("./taxes.csv", "wb")
writer = csv.writer(outfile, delimiter = ';')
writer.writerows(row_list)
reader = csv.reader(outfile)
'''