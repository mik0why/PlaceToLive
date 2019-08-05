import Pandas as pd
'''
I. Data from the user
////////////////////////////////////////////////////////////////////////
part 1: info about yourself

Please enter your occupation
-- should there be a list intially?

Please enter your country, (state), and hometown
-- if: country == USA, then enable state to be chosen

////////////////////////////////////////////////////////////////////////
part 2: what is important to you?
select how important is each of these for you, on a 1-10 scale.
* Salary (per month or per year)
* Proximity to Home
* Days off a year
* National Language same as yours
* Country's HDI
* Sunny Weather (average ??? C / ??? F yearly) - should give more info?
* Crime Rate
* Life Expenses (rephrase ?)
* Life Expectancy
* Taxes


Please enter your occupation 
(should I have a list initally?)

////////////////////////////////////////////////////////////////////////
part 3: data from the web

Need to get each of these from various sources (use rankings?)
ez:
	* HDI
	* Healthcare (Healthcare Access and Quality Index)
	* Weather
	* crime rate
	* life expenses
	* life expectancy


req manual scraping
	* # days off	
	* official language spoken
	* taxes
	---
	* distance from home
	* salary (+ after taxes?)





-----
For tomorrow (6/8):
* scrape the easy data into excel files
* read about designing a drop-down menu in Python
* decide how to create bins & combine the first 9 categories into one table


///How to assign values to each of these?
Maybe: please choose 4 categories that you consider very important
/4 less important / 4 not very important (have a click-on menu?)

Will we need to compute the results for each country?
And simply adjust depending on the weights?
^ that sounds like a good idea - would be good to have a dataframe with all variables
	and the weights are updated by the user. then the math is done to come up with 
	a new table which does not inlcude the data that needs to be scraped with each
	query:
	* salary (again, using bins)
	* distance from home / ticket price (a few bins)
	* your language spoken? (binary variable)




btw describe how you decided to divide each of these into unique bins
* salary
the website found at work; need to decide 

* home prox - need info about flights and their distribution

world's biggest airline - American Airlines (not needed)
into how many bins to divide data? 4/5?
https://www.finder.com/ranked-the-cost-of-air-travel-in-80-countries - play with this


* # days off
https://datatofish.com/read_excel/
scrape data from wikipedia and make some manual changes
https://en.wikipedia.org/wiki/List_of_minimum_annual_leave_by_country

* human development index
http://hdr.undp.org/en/composite/HDI - depending on each category

*health care


-----
display country with its characteristics at the end?

'''