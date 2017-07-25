import urlparse
import requests
import urllib2
import time
import os
import re
import pickle
import random
from datetime import datetime
from bs4 import BeautifulSoup 
from bs4 import SoupStrainer
from bs4 import Comment

# Simulate facebook Login and create an open session
def createSession(userName,password):

	# url from facebook with the hidden form values.  Can be generated through scraping
	# www.facebook.com, but hard coded for convience
	url = "https://m.facebook.com/?stype=lo&jlou=AfeJr_iOaHxWds-5nkpCZt__tCBtVhS4cbH8IgnSdXqcJ0ch6uYQAoMZxzwenCEUcMCCqFGzCbAS8a1e3ZzWSPWv1SVACP5n2NS8wAKyeUtA-Q&smuh=28821&lh=Ac9-YBcjcOplu-oL&_rdr"

	# Step 1: Get request to the login page
	r = requests.get(url)
	html_source = r.text
	soup = BeautifulSoup(html_source,"lxml")

	# Step 2: Get values from the form with the hidden attributes
	# Find the actionpage.php that the form submits to
	action = soup.find('form',id='login_form').get('action')


	# Find other hidden form attributes
	lsd = soup.find('input',{'name' : 'lsd'}).get('value')
	m_ts = soup.find('input',{'name': 'm_ts'}).get('value')
	li = soup.find('input',{'name': 'li'}).get('value')
	try_number = soup.find('input',{'name': 'try_number'}).get('value')

	# Create the dictionary for the requests library form submission
	data = {
		'lsd' : lsd,
		'try_number' : try_number,
		'm_ts' : m_ts,
		'li' : li,
	}

	# Add personal information: info that hitting the server
	# with a get request doesn't provide
	data['email'] = userName
	data['pass'] = password
	data['login'] = 'Log In'

	# hit the action page php with the populated form and establish
	# a session for later requests 
	s = requests.Session()
	s_main = s.post(action, data=data)

	print "session successfully established with facebook"

	return s