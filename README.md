# LazyBook - VERSION ALPHA 

LazyBook is an automated Facebook birthday wisher and data collection tool written in Python 2.7.  It utilizes your Facebook login credentials to collect information from your friends' profiles via web scraping.  While I originally intended to leverage Facebook's API to collect this information, this functionality was depreciated from Facebook's graph API in 2014.  

Ever since I was a young boy, I wanted my friends to realize how much I care and treasure our friendship.  Last year with the power and utility of an introduction to data structures class under my belt, I set off to help my 800+ Facebook friends realize the depths of our friendship by automatically wishing them a happy birthday.  Much to my chagrin, Stack Overflow said this task was impossible - BASH scripts previously written using Facebook's API no longer worked.  But I've always preferred to see no or "that's impossible" as a challenge rather than an answer.  

During my journey to develop an automated Facebook birthday wisher, I realized that we can accomplish so much more than simply wishing people a happy birthday.  For example, the getSingle.py file collects a list of your friends who list single as their relationship status.  unfriendCheck.py compiles a list of friends who you are no longer friends with (updated each month).  I encourage you to expand on the examples I provide and open pull requests with your contributions.  After all, we're all in need of a poke-war bot.

## Getting Started

This script is fairly straight forward - all it requires is the installation of several common python libraries (Beautiful Soup, etc.) each of which can be installed with a single line in your terminal.  I've also included the code to set up a scheduled task: all you need to do is load and launch it.  Lastly, I apologize for only including a tutorial macOS.  A windows tutorial is on my TODO list, and if you're running a linux OS, then you probably don't need a tutorial anyway.  

### Installing Libraries

Setup is fairly simple, all we need to do is install several common python libraries.  You can follow either of the following procedures:

Option 1: In your command terminal, navigate inside of your LazyBook folder and type ```pip install -r requirements.txt```

Option 2:  In your command terminal type the following:

```
pip install bs4
```

```
pip install requests
```

```
pip install lxml
```

### Variable Flags

#### main.py
In main.py there are several boolean variables that you can set

```
userName = "your_username/email"
```
* This should the username or email you use to login to Facebook.  Enter it between the quotation marks.

```
password = "your_password"
```
* This should be the password you use to login to Facebook.  Enter it between the quotation marks.

```
metaData['wishBirthday'] = True
```
* This flag determines whether you post on your friend's wall for his or her birthday.  If it is off, then you will not post (even if you set up the scheduled task)
* Change to False if you do not want to wish your friends a happy birthday every day (also requires you to set up the scheduled task described in the following section)

```
metaData["getSingle"] = True
```
* This flag determines if you create a list of friends who are single (saved under the Structs folder in single.txt)
* Change to False if you do not want to collect this information (also will take a long time to complete since I haven't upgraded it to use concurrency)
* Note: this function will not run if you already have a list of friends (saved as Single.txt in the Structs folder) even if it is set to True.  If you want to run this function after the first time, then you need to manually delete the single.txt file.

```
metaData["unfriendCheck"] = True
```
* This flag determines if you keep track of the people you are no longer friends with on Facebook 
* Change to false if you do not want this information.
* Note: this list is updated once a month (and updates your friends list saved information once a month) if set to True.

```
ignoreList = ["first_name last_name", "first_name last_name", "first_name last_name"]
```
* Add names between the quotation marks as they appear on Facebook if you do not want to wish them a happy birthday.
* This field is only relevant if metaData['wishBirthday'] = True
* If you later decide to add or remove names from this list, navigate into the Structs folder and delete metaData.pkl.  The next time the script is run, it will update your ignoreList

#### wishBirthday.py

At the bottom of this file, there is a list named messages.  Modify this list as you see fit to customize or add new messages.  Each message has an equal probability of being chosen.  After the message is chosen, there is a 50% chance that it is posted to your friend's wall.  The other 50% is a message that says "Happy Birthday first_name!".  You can modify this other 50% in the wish method in the same file. 

### Setting up an automated task (macOS) 
0. Open org.lazybook.birthday.plist in your favorite text editor and change "YOUR_USERNAME_HERE" to your mac user account name (the one that appears when you type in `echo $USER` or `whoami` in your terminal.
1. Copy org.lazybook.birthday.plist
2. Navigate to ~Library/LaunchAgents/ in finder (this may require to unhide the Library folder in your settings)
3. Paste org.lazybook.birthday.plist into this directory
4. Open your terminal and navigate to ~/Library/LaunchAgents
5. Load your script into the macOS task scheduler by typing "launchctl load ~/Library/LaunchAgents/org.lazybook.birthday.plist" in your terminal 
6. Start your script by typing "launchctl start org.lazybook.birthday" into the terminal
7. After step 6, the task scheduler will immediately wish your friends a happy birthday, and then once again every 24 hours until you stop it
8. You can view the status of your task by typing `launchctl list | grep birthday`
9. To stop the automated task (and thereby the python script from running), navigate to  ~Library/LaunchAgents/ in your terminal and type `launchctl remove org.lazybook.birthday`

* [Helpful Resource for starting tasks](http://killtheyak.com/schedule-jobs-launchd/)
* [Helpful Resource for stopping tasks](http://osxdaily.com/2011/03/08/remove-an-agent-from-launchd/)

## Bugs List

* N/A so far

## TODO List

* Switch over username and password from in-line code to environment variables (and update documentation)
* Create a GUI!!!
* rewrite in Python 3
* write a Getting Started tutorial for windows users
* create youtube video that walks through the Getting Started steps for beginners
* Update getSingle function so it uses python's concurrency (like in getFriends and getBirthdays) and doesn't take 5+ minutes to complete
* Collect posts by friends and run through a binary classifier (i.e. spam filter) to determine if a friend is "spam" or "not spam"

## License
Feel free to use this software in any legal endeavors or projects - just link back to this repo to acknowledge my work and help other developers find this script (licensed under MIT License).

## Final Thoughts

 Please don't misuse this script! It's meant to be a fun little tool to help your friends realize how much you care about them and gather data for analytics (ideally in your personal projects).  Could you modify it to do something annoying? Yes.  Please don't be an asshole.  If this becomes an issue for Facebook, then they will easily fix it.  If you're a Facebook engineer reading this, please enjoy :)

Finally, is this legal?  Yes!  Very much so!  I sent an email to Facebook's security department a while back, and they do not view this script as a concern or security violation since it does not collect private information.  We're not going anywhere we're not supposed to go, and we can collect all of this information by clicking through profiles and recording it.  We're simply automating a tiresome task.  I personally don't log into Facebook every day, but would like to wish my friends a happy birthday even when I don't log in.

If you would like to contact me to contribute or just talk, then you can reach me at cfifty.github@gmail.com.  If you enjoy using this script and would like more like it then please donate [here](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=4WHNCY5Z4GZPJ&lc=US&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted). All funds will go towards alleviating the crushing weight of student loans, my weekly coffee budget, and allowing me to work fewer hours for my university's work-study program.

