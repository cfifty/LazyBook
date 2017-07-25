import getFriends
import os
import pickle


def check(s): 
	# Get our friendsDict
	structDir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Structs'))
	with open(structDir + '/friendsDict.pkl','rb') as input:
		friendsDict = pickle.load(input) 

	# redownload our friends list
	getFriends.consolidateFriends(s)
	with open(structDir + '/friendsDict.pkl','rb') as input:
		friendsDict2 = pickle.load(input) 	

	diff = []
	for friend in friendsDict:
		if friend not in friendsDict2:
			diff.append(friend)

	unfriendList = []
	# if we have a list of people who have unfriended us
	if(os.path.isfile(structDir + '/unfriendList.pkl')):
		with open(structDir + '/unfriendList.pkl','rb') as input:
			unfriendList = pickle.load(input) 			

	for friend in diff:
		if friend not in unfriendList:
			temp = friend.encode('utf-8').strip()
			unfriendList.append(temp + "\n")

	# update our unfriendLst data structure
	structDir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Structs'))
	with open(structDir + '/unfriendList.pkl', 'wb') as f:
		pickle.dump(unfriendList, f, pickle.HIGHEST_PROTOCOL)

	# now generate a text file for easy reading..
	unfriendStr = ''.join(diff)
	
	with open(structDir + "/unfriend.txt","wb") as file1: 
		file1.write(unfriendStr)