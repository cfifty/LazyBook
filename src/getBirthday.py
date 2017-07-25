import urlparse
import requests
import urllib2
import time
import re
import os
import pickle
import threading
from bs4 import BeautifulSoup 
from bs4 import SoupStrainer
from bs4 import Comment

def getFriendsBirthdays(birthdays,friendsDict,s): 

# --------- Getting Birthday Info -----------
	relatStrainer = SoupStrainer(text=re.compile("Birthday"))
	relatExt = "/about"
	relatExtBeta = "&sk=about"
	fbook = "https://facebook.com"	

	#***** Note: will have to perform additional string methods because scraping from main page
	for friend in friendsDict: 
		if (friendsDict[friend].find("php") != -1):
			relatURL = fbook + friendsDict[friend] + relatExtBeta
		else:
			relatURL = fbook + friendsDict[friend] + relatExt

		relatInfo = s.get(relatURL)
		soup = BeautifulSoup(relatInfo.text,"lxml",parse_only=relatStrainer)

		subString = soup.find(text=re.compile("Birthday"))
	
		if (subString != None):
			# Cut off everthing before Birthday
			stringIndex = subString.find('Birthday')
			subString = subString[stringIndex:]

			# Cut off the prefix to get the birthdate and everything after
			stringIndex = subString.find('<div>')
			subString = subString[(stringIndex+5):]

			# Get rid of everything after the birthday
			stringIndex = subString.find('</div>')
			subString = subString[:stringIndex]

			# Standardize the birthday date by cutting off the year if there is one
			commaIndex = subString.find(',')
			if (commaIndex != -1):
				subString = subString[:commaIndex]

			if (subString in birthdays):
				birthdays[subString].append(friend)
			else:
				birthdays[subString] = [friend]

			print friend + " has birthday " + subString
	return

def consolidateBirthdays(s):
	birthday0 = {}	
	birthday1 = {}
	birthday2 = {}
	birthday3 = {}
	birthday4 = {}
	birthday5 = {}
	birthday6 = {}
	birthday7 = {}
	birthday8 = {}
	birthday9 = {}
	friends0 = {}
	friends1 = {}
	friends2 = {}
	friends3 = {}
	friends4 = {}
	friends5 = {}
	friends6 = {}
	friends7 = {}
	friends8 = {}
	friends9 = {}

	# Get our friendsDict
	structDir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Structs'))
	with open(structDir + '/friendsDict.pkl','rb') as input:
		friendsDict = pickle.load(input)

	iterator = 0
	for friend in friendsDict: 
		if(iterator < len(friendsDict)/10):
			friends1[friend] = friendsDict[friend]
		elif(iterator < len(friendsDict)/5):
			friends2[friend] = friendsDict[friend]
		elif(iterator < 3*len(friendsDict)/10):
			friends3[friend] = friendsDict[friend]
		elif(iterator < 4*len(friendsDict)/10):
			friends4[friend] = friendsDict[friend]
		elif(iterator < len(friendsDict)/2):
			friends5[friend] = friendsDict[friend]
		elif(iterator < 6*len(friendsDict)/10):
			friends6[friend] = friendsDict[friend]
		elif(iterator < 7*len(friendsDict)/10):
			friends7[friend] = friendsDict[friend]
		elif(iterator < 8*len(friendsDict)/10):
			friends8[friend] = friendsDict[friend]
		elif(iterator < 9*len(friendsDict)/10):
			friends9[friend] = friendsDict[friend]
		else:
			friends0[friend] = friendsDict[friend]
		iterator += 1

	# 4 threads -> 101.25 s
	# 6 threads -> 68 s
	# 10 threads -> 42.7s
	t0 = threading.Thread(target=getFriendsBirthdays,args=(birthday0,friends0,s,))
	t1 = threading.Thread(target=getFriendsBirthdays,args=(birthday1,friends1,s,))
	t2 = threading.Thread(target=getFriendsBirthdays,args=(birthday2,friends2,s,))
	t3 = threading.Thread(target=getFriendsBirthdays,args=(birthday3,friends3,s,))
	t4 = threading.Thread(target=getFriendsBirthdays,args=(birthday4,friends4,s,))
	t5 = threading.Thread(target=getFriendsBirthdays,args=(birthday5,friends5,s,))
	t6 = threading.Thread(target=getFriendsBirthdays,args=(birthday6,friends6,s,))
	t7 = threading.Thread(target=getFriendsBirthdays,args=(birthday7,friends7,s,))
	t8 = threading.Thread(target=getFriendsBirthdays,args=(birthday8,friends8,s,))
	t9 = threading.Thread(target=getFriendsBirthdays,args=(birthday9,friends9,s,))

	# start_time = time.time()
	t0.start()
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()
	t6.start()
	t7.start()
	t8.start()
	t9.start()
	t0.join()
	t1.join()
	t2.join()
	t3.join()
	t4.join()	
	t5.join()
	t6.join()
	t7.join()
	t8.join()
	t9.join()
	# print("--- %s seconds ---" % (time.time() - start_time))
	

	# manually update the birthdays dict because the default dict.update 
	# overwrites the entries
	birthdays = dict(birthday1) 
	for a in birthday2:
		if a in birthdays:
			birthdays[a] = birthdays[a] + birthday2[a]
		else:
			birthdays[a] = birthday2[a]
	for a in birthday3:
		if a in birthdays:
			birthdays[a] = birthdays[a] + birthday3[a]
		else:
			birthdays[a] = birthday3[a]	
	for a in birthday4:
		if a in birthdays:
			birthdays[a] = birthdays[a] + birthday4[a]
		else:
			birthdays[a] = birthday4[a]
	for a in birthday5:
		if a in birthdays:
			birthdays[a] = birthdays[a] + birthday5[a]
		else:
			birthdays[a] = birthday5[a]
	for a in birthday6:
		if a in birthdays:
			birthdays[a] = birthdays[a] + birthday6[a]
		else:
			birthdays[a] = birthday6[a]
	for a in birthday7:
		if a in birthdays:
			birthdays[a] = birthdays[a] + birthday7[a]
		else:
			birthdays[a] = birthday7[a]
	for a in birthday8:
		if a in birthdays:
			birthdays[a] = birthdays[a] + birthday8[a]
		else:
			birthdays[a] = birthday8[a]
	for a in birthday9:
		if a in birthdays:
			birthdays[a] = birthdays[a] + birthday9[a]
		else:
			birthdays[a] = birthday9[a]
	for a in birthday0:
		if a in birthdays:
			birthdays[a] = birthdays[a] + birthday0[a]
		else:
			birthdays[a] = birthday0[a]

#	for birthday in birthdays:
	#	print "birthday " + str(birthday) + " corresponds to " + str(birthdays[birthday])
	

	# Save our birthdays dictionary to a file in our directory
	with open(structDir + '/birthdays.pkl', 'wb') as f:
		pickle.dump(birthdays, f, pickle.HIGHEST_PROTOCOL)

	print "successfully saved friends' birthdays"