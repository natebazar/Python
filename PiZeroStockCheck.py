# PythonProjects
# PiZero Stock Checker
import urllib2
from bs4 import BeautifulSoup
import re
import time, threading

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Google Chrome')]

def CheckStock(url, name):
	ourUrl = opener.open(url).read()
	soup = BeautifulSoup(ourUrl, "html.parser")
	title = soup.title.text
	body = soup.find(text="OUT OF STOCK")	   #Searches for text
	tag_pr = soup.find(id="prod-price").string
	price = ' '.join(tag_pr.split())
	tag_stk = soup.find(id="prod-stock").findNext(id="prod-stock").next_element #Find second item with id and set value to its next element.
	stock = ""
	if tag_stk:
		stock = ' ' .join(tag_stk.split())		#Get rid of tabs and newlines. Joins elements by space.
	else:
		stock = "Couldn't find that..."
	
	if body:									#If the text is found on the page, do stuff.
		print name
		print "...............Price:",price
		print "...............Stock: Out of Stock\n"
	else:
		print name
		print "...............Price:",price
		print "...............Stock:",stock


def Check(interval):
	
	url = ('https://www.adafruit.com/products/2885')
	name = "PiZero".ljust(15)
	CheckStock(url,name)

	url = ('https://www.adafruit.com/product/2816')
	name = "PiZero Starter".ljust(15)
	CheckStock(url,name)

	url = ('https://www.adafruit.com/product/2817')
	name = "PiZero Budget".ljust(15)
	CheckStock(url,name)
	
	#threading.Timer(interval,Check).start()

Check(120)	
