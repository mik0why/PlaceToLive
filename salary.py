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
			value = item


	scrape_to_csv(value) #ok for now but later will be modified

#wage_scrape("Marketing")

#now import all the salaries from around the world to the doc


def scrape_to_csv(idx):
	#step 1 - organize all the countries
	'''
	url = "http://www.salaryexplorer.com"
	soup = BeautifulSoup(url)
	ctr = soup.find('div', attrs = {"class": "whiteblock"})
	print ctr
	'''


	for i in range(244):
		url = "http://www.salaryexplorer.com/salary-survey.php?loc=" + str(i) + "&loctype=1&job=" + str(idx) + "&jobtype=1"
		response = requests.get(url) #three crucial lines for BeautifulSoup to work
		html = response.content
		soup = BeautifulSoup(html)
		yah = soup.find('div', attrs = {"class" : "youarehere"})
		country = yah.findAll('a')[0].contents[0].string
		print country

		slr = soup.find('div', attrs = {"class" : "salaryblock floatedsalary"})
		print slr #get the content of the img tag?
		#why does it print "All Jobs" initially?


		#	if country == "All Jobs":
			#ignore somewhow?
			#btw decide on which countries should be ignored bc not present in other tables
			#for some, ex. Vatican City State, might add to the table with a changed name (ex. Vatican)
			#salary
			# currency

	#print url
	#print yah
	#print i,
	 
# loc needs to iterate
#job is obtained from 
#scrape_to_csv(40)


		'''
		outfile = open("./taxes.csv", "wb")
		writer = csv.writer(outfile, delimiter = ';')
		writer.writerows(row_list)
		reader = csv.reader(outfile)
		'''