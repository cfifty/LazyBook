import urlparse
import requests
import urllib2
import time
import re
import pickle
import random
import os
from datetime import datetime
from bs4 import BeautifulSoup 
from bs4 import SoupStrainer
from bs4 import Comment

# wish your friend a birthday
def wish(s):
	structDir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Structs'))

	conversion = ['January','February','March','April','May','June',
	'July','August','September','October','November','December']
	
	today = datetime.now()
	month = conversion[(today.month -1)]
	day = str(today.day)
	date = month + " " + day

	# Get our birthdays list
	with open(structDir + '/birthdays.pkl','rb') as input:
		birthdays = pickle.load(input)

	# Get our friendsDict
	with open(structDir + '/friendsDict.pkl','rb') as input:
		friendsDict = pickle.load(input)


	for name in birthdays[date]:
		prefix = 'https://m.facebook.com'
		vanity = friendsDict[name]
		url = prefix + vanity
		temp = s.get(url)
		soup = BeautifulSoup(temp.text,"lxml")
		html = soup.prettify("utf-8")

		# Populate the form with appropriate hidden values
		action = 'https://m.facebook.com' + soup.find('form',{'method' : 'post'}).get('action')
		fb_dtsg = soup.find('input',{'name' : 'fb_dtsg'}).get('value')
		fbook_id = soup.find('input',{'name': 'id'}).get('value')
		xhpc_timeline = soup.find('input',{'name': 'xhpc_timeline'}).get('value')
		target = soup.find('input',{'name': 'target'}).get('value')
		c_src = soup.find('input',{'name': 'c_src'}).get('value')
		cwevent = soup.find('input',{'name': 'cwevent'}).get('value')
		referrer = soup.find('input',{'name': 'referrer'}).get('value')
		ctype = soup.find('input',{'name': 'ctype'}).get('value')
		cver = soup.find('input',{'name': 'cver'}).get('value')


		# Create the dictionary for the requests library form submission
		data2 = {
			'fb_dtsg' : fb_dtsg,
			'id' : fbook_id,
			'xhpc_timeline' : xhpc_timeline,
			'target' : target,
			'c_src' : c_src,
			'cwevent' : cwevent,
			'referrer' : referrer,
			'ctype' : ctype,
			'cver' : cver,
		}

		with open(structDir + '/birthdayMessages.pkl','rb') as input:
			messages = pickle.load(input)

		# select a random number for the random birthday message
		r = random.randrange(0,(len(messages)))
		if(r < (len(messages)/2)):
			if(name.find(' ') != -1):
				data2['xc_message'] = 'Happy Birthday ' + name[:name.find(' ')] + '!'
			else:
				data2['xc_message'] = messages[r]
		else:
			data2['xc_message'] = messages[r]

		# Add personal information
		data2['view_post'] = "Post"

		s2 = s.post(action, data=data2)
		print("Wished " + name + " a happy birthday!")

	print "Finished wishing birthdays"


# Predetermined list of birthday wishes to send
def createBirthdayWishes(): 
	messages = ["Happy Birthday", "Happy Birthday!", "Happy Birthday!!",
				"Happy Birthday!!!", "Happy Birthday!!!!", "happy birthday!"]

	structDir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Structs'))
	with open(structDir + '/birthdayMessages.pkl', 'wb') as f:
		pickle.dump(messages, f, pickle.HIGHEST_PROTOCOL)

	print "finished creating several birthday wishes..."



