#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import csv
from lxml.html.soupparser import fromstring
import json
import sys
#To-Do: the conversion between each currency to USD dollars
#status code 200 - successful req
# req packages: google



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


	scrape_to_csv(value) #ok for now but later will be modified

def scrape_to_csv(idx):






	#print data	


	#print data.items().get("USD")
	#print data['rates']

	row_list = []
	for i in range(5): #TODO changed from 244
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


			#look into fixer.io



			#print url2
			#resp2 = requests.get(url2)
			#html_2 = requests.get(url2).content #.content
			#print html_2 #.content
			#soup2 = BeautifulSoup(html_2, 'html5lib')#, 'html.parser')
			#maybe data is invalid?

			#soup2 = fromstring(BeautifulSoup(html_2))
			#print soup2
			'''
			rate = soup2.find('div', attrs = {"id" : "reactContainer"}) #up to here ok, but later idk why it doesn't work
			if rate is not None:
				rate_2 = rate.find('div')
				print rate_2
			#not finding this div
			print rate
			'''

			col_list.append(i)
			col_list.append(country)
			col_list.append(wage_curr[0].replace(",", "")) #be careful with all that replacing
			col_list.append(wage_curr[1])
			#col_list.append(convRate)
		row_list.append(col_list)

#	print get_key()


	#obj = "http://data.fixer.io/api/symbols ? access_key = " + get_key()
	obj = "http://data.fixer.io/api/latest?access_key="+ get_key()

	#print obj



	resp = requests.get(obj)
	data = resp.json()
	entries = json.dumps(data.items()[3])
	#data = json.dump(data, sys.stdout)["USD"]	
	#print entries

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

	#value = []


	#case when the currency is EUR
	print exch_curr


	if "EUR" in exch_curr:
		print "juro!!!"
		ex_rate = float(eur_usd)
		ex_val = float(wage_curr[0].replace(',', ""))

	else:
		end_point = len(exch_curr) - 1
		start_point = 0
		for i in range(len(exch_curr)):
			if(exch_curr[i].isdigit()):
				start_point = i
				break
		
			print "length : {} + start: {} + end : {}".format(len(exch_curr), start_point, end_point)


			ex_val = exch_curr[start_point:end_point]
			print ex_val
			print float(ex_val) / 2.0
			ex_rate = float(eur_usd) / float(ex_val)

	wage_curr[0] = wage_curr[0].replace(',', "")

	print "{} val: {}\n USD val : {}".format(wage_curr[1], ex_val, eur_usd)
	print" {} to USD: {}".format(wage_curr[1], ex_rate)
	print"income : {}".format(float(wage_curr[0]) * ex_rate) #the actual income in USD

			#i tutaj dodaj aktualna currency na eur
			#potem zamien :)

		#	print val

#append each currency converter to the col_list - but how to do it for the existing ones?



	outfile = open("./salary.csv", "wb")
	writer = csv.writer(outfile, delimiter = ';')
	writer.writerows(row_list)
	reader = csv.reader(outfile)
