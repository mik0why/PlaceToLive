#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import csv
from lxml.html.soupparser import fromstring
import json
import sys
import pandas as pd
import os
#To-Do: the conversion between each currency to USD dollars
#TO-DO: problem with Virgin Islands (British & US)

def get_key():
	key_file = open("key.txt")
	return key_file.readline().rstrip()
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
def scrape_to_csv(idx):

	row_list = []
	for i in range(244):
		#maybe should print the percentage & clear the screen as in the prev project
		col_list = []
		
		url = "http://www.salaryexplorer.com/salary-survey.php?loc=" + str(i) + "&loctype=1&job=" + str(idx) + "&jobtype=1"
		response = requests.get(url) #three crucial lines for BeautifulSoup to work
		html = response.content
		soup = BeautifulSoup(html, 'lxml')

		yah = soup.find('div', attrs = {"class" : "youarehere"})
		country = yah.findAll('a')[0].contents[0].string
		if country != "All Jobs": 
			slr = soup.find('div', attrs = {"class" : "salaryblock floatedsalary"}) #getting the salary
			wage_curr = str.split(slr.contents[2].encode('utf-8'))
			print country, wage_curr[0], wage_curr[1] #number

			entry = wage_curr[0] + " "  + wage_curr[1] + " to USD"
			print entry.encode("utf-8")

			col_list.append(i)
			col_list.append(country)
			col_list.append(wage_curr[0].replace(",", "")) #be careful with all that replacing
			col_list.append(wage_curr[1])
			#col_list.append(convRate)

			#obj = "http://data.fixer.io/api/symbols ? access_key = " + get_key()
			obj = "http://data.fixer.io/api/latest?access_key="+ get_key()

			# add a try catch block here?
			resp = requests.get(obj)
			data = resp.json()
			entries = json.dumps(data.items()[3])

			start = 0
			end =  0
			all_str =[]
			curr_str = []
			
			for i in range(len(entries)):
				start = end
				if entries[i] != ',':
					curr_str.append(entries[i])
				else:
					end = i
					all_str.append("".join(curr_str))

					curr_str = []

			print "currency: " + wage_curr[1]

			for i in range(len(all_str)):
				if "USD" in all_str[i]:
					eur_usd = all_str[i][8:] # USD to EUR 
				elif wage_curr[1] in all_str[i]:
					exch_curr = all_str[i]
					#look into how this is extracted, has extra symbol
					# but FIRST: take a step back and re-organize this method 


			print "got : " + eur_usd + " , " + exch_curr

			#case when the currency is EUR - need to extract only the digits
			if "EUR" in exch_curr:
				print "juro!!!"
				ex_rate = float(eur_usd)
				ex_val = float(wage_curr[0].replace(',', ""))

			else:
				end_point = len(exch_curr) - 1
				start_point = 0
				for a in range(len(exch_curr)):
					#print exch_curr[a] + "\n"
					if(exch_curr[a].isdigit()):
						start_point = a
						break
				


				ex_val = exch_curr[start_point:end_point]
				print ex_val
				print float(ex_val) / 2.0
				ex_rate = float(eur_usd) / float(ex_val)

			wage_curr[0] = wage_curr[0].replace(',', "")

			print "{} val: {}\n USD val : {}".format(wage_curr[1], ex_val, eur_usd)
			print" {} to USD: {}".format(wage_curr[1], ex_rate)
			print"income : {}".format(float(wage_curr[0]) * ex_rate) #the actual income in USD
			col_list.append(int(int(wage_curr[0]) * ex_rate))
			print '*************'


		row_list.append(col_list)
	outfile = open("./salary.csv", "wb")
	writer = csv.writer(outfile, delimiter = ';')
	writer.writerows(row_list)
	reader = csv.reader(outfile)
def csv_salary_organize():
	df = pd.read_csv("./salary.csv", header = None, delimiter=';')
	df.rename(columns = {0: 'idx', 1: 'Country', 2: 'Salary', 3: 'Currency', 4: 'Salary[USD]'}, inplace = True)
	df.sort_values(by = 'Salary[USD]', inplace = True, ascending = False)
	
	# the last thing - reset values of 'idx'
	df.to_excel("sorted_salaries.xlsx", index = False) #should it have the prof in the name?
	'''
	df.to_csv("sorted_salaries.csv", index = True)#, delimiter = ';')	
	outfile = open("./sorted_salaries.csv", "wb")
	reader = csv.reader(outfile)
	'''

csv_salary_organize() # just now for testing
if(os.path.isfile('sorted_salaries.xlsx') == False): #should the name have occupation in it?
	if(os.path.isfile('./salary.csv') == False):
		scrape_to_csv(value) #scrape first
	csv_salary_organize()