import urlparse
import requests
import urllib2
import time
import os
import sys
import re
import pickle
import threading
from datetime import datetime
from bs4 import BeautifulSoup 
from bs4 import SoupStrainer
from bs4 import Comment


# Function to get the friends list and save it to a file
def getFriendsList(friends, part,s):
	ID = vanity
	if(part == 1):
		index = 0;
	elif(part == 2): 
		index = 24;
	elif(part == 3):
		index = 24+36
	else:
		index = 24+36+36

	# find scrape their total number of friends
	temp = s.get('https://www.facebook.com/' + ID + '/friends')
	soup = BeautifulSoup(temp.text,"lxml")
	strainer = SoupStrainer('a',href=re.compile("fref=fr_tab"))

	# iterator over entire friends list and pull out the relevant information from 
	# the html docs that display 24 or 36 friends each
	while (index < (numFriends)): 
		if index == 0:
			temp = s.get('https://m.facebook.com/' + ID + '/friends')
			soup = BeautifulSoup(temp.text,"lxml",parse_only=strainer)
			tempLst = soup.findAll('a')
			for item in tempLst:
				friends.append(item)
			index = 24 + 36*3
		else: 
			temp = (s.get('https://m.facebook.com/' + ID + '/friends?startindex='
				+ str(index)))
			soup = BeautifulSoup(temp.text,"lxml",parse_only=strainer)
			tempLst = soup.findAll('a')
			for item in tempLst:
				friends.append(item)
			index = index + 36*4
	return 

def consolidateFriends(s): 
	
	# we need to get you're facebook unique identifier i.e. vanity
	temp = s.get('https://www.facebook.com')
	soup = BeautifulSoup(temp.text,"lxml")
	html = soup.prettify("utf-8")
	href = soup.find('a', {"title" : "Profile"}).get('href')
	global vanity
	vanity = href[25:]

	# scrape the number of friends that you have
	temp = s.get('https://www.facebook.com/' + vanity)
	soup = BeautifulSoup(temp.text,"lxml")
	comments=soup.findAll(string=lambda text:isinstance(text,Comment))
	soup = BeautifulSoup(comments.pop(2),"lxml")
	global numFriends
	numFriends = int(soup.find('a', {'data-tab-key' : 'friends'}).span.text)
#	with open("output.html","wb") as file: 
	#	file.write(html)



	friends1 = []
	friends2 = []
	friends3 = []
	friends4 = []
	t1 = threading.Thread(target=getFriendsList,args=(friends1,1,s,))
	t2 = threading.Thread(target=getFriendsList,args=(friends2,2,s,))
	t3 = threading.Thread(target=getFriendsList,args=(friends3,3,s,))
	t4 = threading.Thread(target=getFriendsList,args=(friends4,4,s,))
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t1.join()
	t2.join()
	t3.join()
	t4.join()

	friends = friends1 + friends2 + friends3 + friends4
	friendsDict = {}
	iterator = 1

	# Iterate over output from html friends list and extract valid information
	# and add it to a dictionary 
	for friend in friends:
		name = friend.text
		ext = friend['href']
		strIndex = ext.find("fref=fr_tab")
		ext = ext[0:strIndex]
		if (ext.find("?") == (len(ext) - 1)):
			strIndex = ext.find("?")
			ext = ext[0:strIndex]
		elif (ext.find("&") == (len(ext) - 1)):
			strIndex = ext.find("&")
			ext = ext[0:strIndex]
		friendsDict[name] = ext
		# print "Iteration " + str(iterator) +" "+ name + " corresponds to " + ext
		iterator += 1

	structDir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Structs'))
	with open(structDir + '/friendsDict.pkl', 'wb') as f:
		pickle.dump(friendsDict, f, pickle.HIGHEST_PROTOCOL)

	print "successfully mapped friends name to vanity"
