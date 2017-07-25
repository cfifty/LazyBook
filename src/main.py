import getSession
import getFriends
import getBirthday
import wishBirthday
import getSingle
import unfriendCheck
import os
import pickle
from datetime import datetime

structDir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Structs'))
metaData = {}

# enter your facebook username and password here
userName = "username"
password = "password"

# if there is no saved metadata
if not os.path.isfile(structDir + '/metaData.pkl'):

	# ------ User settings - change to true in order to enable ------

	# set wish birthday to false if you do not want to wish your friends a happy birthday every day
	metaData["wishBirthday"] = True

	# set getSingle to false if you do not want a list of your single friends
	metaData["getSingle"] = True

	# add names (as they appear on facebook) to the ignore list to not wish these friends a happy birthday
	ignoreList = ["first_name last_name", "first_name last_name", "first_name last_name"]

	# set unfriendCheck to true if you want to keep track of the friends who unfriend you
	# currently checks at the end of every month
	metaData["unfriendCheck"] = True

	# Please look at the createBirthdayWishes method in wishBirthday.py to create customized birthday messages
	wishBirthday.createBirthdayWishes()

	# get the current date and time
	savedDate = datetime.now()
	# ------ end user settings ------

	# save settings in meta-data
	with open(structDir + '/metaData.pkl', 'wb') as f:
		pickle.dump(metaData, f, pickle.HIGHEST_PROTOCOL)

	# save the ignore list 	
	with open(structDir + '/ignoreLst.pkl','wb') as f:
		pickle.dump(ignoreList, f, pickle.HIGHEST_PROTOCOL)

	# save the current date
	f = open(structDir + '/savedDate.pkl','wb')
	pickle.dump(savedDate,f)
	f.close()

# ---- The part run once a day ----
with open(structDir + '/metaData.pkl','rb') as input:
	metaData = pickle.load(input)

# automatically create a session for any of your actions.
s = getSession.createSession(userName,password)

# if you set wishBirthday = true, then wish your friends a happy birthday
if metaData["wishBirthday"] == True:
	# if you have a friendsDictionary and birthdaysDictionary file, then just wish them a happy birthday
	if os.path.isfile(structDir + '/friendsDict.pkl') and os.path.isfile(structDir + '/birthdays.pkl'):
		wishBirthday.wish(s)
	else: 
		getFriends.consolidateFriends(s)
		getBirthday.consolidateBirthdays(s)
		wishBirthday.wish(s)


# if you set getSingle to true, then we'll generate a list of your single friends if you don't already have one
if metaData["getSingle"]:
	# if we already have a list of our single friends, then do nothing
	if not os.path.isfile(structDir + '/single.txt'):
		getSingle.getSingle(s)


# if you set unfriendCheck to true and a month has passed, we'll see if friends unfriended you
if metaData["unfriendCheck"]: 
	# if a month, or more than a month has passed
	today = datetime.now()

	#with open(structDir + '/savedDate.pkl','rb') as input:
		#savedDate = pickle.load(savedDate)
	f = open(structDir + '/savedDate.pkl','rb')
	savedDate = pickle.load(f)
	f.close()

	nextMonth = savedDate.month + 1
	if savedDate.month == 12:
		nextMonth = 1
	savedDate = savedDate.replace(month=nextMonth)

	# if at least a month has passed, update the unfriend structure
	if(today >= savedDate):
		print "going into unfriendCheck..."
		# update our saved date...
		with open(structDir + '/savedDate.pkl', 'wb') as f:
			pickle.dump(today,f,pickle.HIGHEST_PROTOCOL)

		unfriendCheck.check(s)

print "ending script"
