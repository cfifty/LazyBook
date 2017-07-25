import os
import pickle
import re
from bs4 import BeautifulSoup 
from bs4 import SoupStrainer
# TODO: update with concurrency.  
# Good proof of concept to show how much faster it is with multithreading though...

def getSingle(s):

	# load in your friends dictionary
	structDir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Structs'))
	with open(structDir + '/friendsDict.pkl','rb') as input:
		friendsDict = pickle.load(input)

	# -------------- Now, let's compile a list of friends who are single ------------
	Single = []
	iteration = 1
	relatStrainer = SoupStrainer(text=re.compile("Single</div>"))
	relatExt = "/about?section=relationship&pnref=about"
	relatExtBeta = "&sk=about&section=relationship"
	fbook = "https://facebook.com"


	for friend in friendsDict: 
		if (friendsDict[friend].find("php") != -1):
			relatURL = fbook + friendsDict[friend] + relatExtBeta
		else:
			relatURL = fbook + friendsDict[friend] + relatExt

		relatInfo = s.get(relatURL)
		soup = BeautifulSoup(relatInfo.text,"lxml",parse_only=relatStrainer)
		comment = soup.find(text=re.compile("Single</div>"))
		if (comment != None):
			# since some names have special characters, we need to strip these
			temp = friend.encode('utf-8').strip()
			Single.append(temp + "\n")
		print friend + " is single = " + str(comment != None)
		# print iteration
		iteration += 1

	# print Single

	singleStr = ''.join(Single)
	
	with open(structDir + "/single.txt","wb") as f: 
		f.write(singleStr)