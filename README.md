# LazyBook - VERSION ALPHA 

LazyBook is an automated facebook birthday wisher and data collection tool written in Python 2.7.  It uses your facebook profile to collect information about your friends via web scraping since this information was depreciated from Facebook's graph API in 2014.  While stack overflow said it was impossible, I wanted to automate wishing my facebook friends a happy birthday - after all, they should know how much I care about them and treasure our friendship (even when I don't log into facebook to specifically wish them a happy birthday).  As a result, I developed this script with the primary goal fo automating the process of wishing my freinds a happy birthday.  During the development process, I realized that we can accomplish so much more than simply wishing people a happy birthday.  I've included additional methods (getSingle and unfriendCheck) as proof of concepts and demonstrations on how information can be collected from your friends.  getSingle saves a text file of the friends who's relationship status is single on facebook and unfriendCheck compiles a list of people I am no longer friends with (updated at the end of every month).  

## Getting Started

Take a look at the following instructions for getting this script up and running.  It is created in Python 2.7 and only requires the download of a few external libraries (i.e. beautiful soup for scraping).  Please note that all instructions are for a computer running macOS.  A tutorial for windows is on my todo list (and if you're running linux, you probably don't need this tutorial anyway).

### Installing Libraries

TODO

```
rewrite when I set this up on a new computer.
```

### Setting Variables in the code

#### main.py
In main.py there are several variables you can set.

```
userName = "your_username/email"
```
* This should the username or email you use to login to facebook.

```
password = "your_password"
```
* This should be the password you use to login to facebook.

```
metaData['wishBirthday'] = True
```
* This flag determines whether you post on your friend's wall for his or her birthday
* Change to False if you do not want to wish your friends a happy birthday every day (also requires you to set up the scheduled task described in the following section)

```
metaData["getSingle"] = True
```
* This flag determines if you create a list of friends who are single (saved under structs in single.txt)
* Change to False if you do not want to get this information
* Note: this function will not run if you already have a list of friends (saved as Single.txt in the Structs folder) even if it is set to True.  If you want to run this function after the first time, then you need to manually delete the single.txt file

```
metaData["unfriendCheck"] = True
```
* This flag determines if you keep track of the people you are no longer friends with on facebook 
* Change to false if you do not want this information.
* Note: this list is updated once a month (and updates your friends list saved information once a month) if set to True.

```
ignoreList = ["first_name last_name", "first_name last_name", "first_name last_name"]
```
* add names as they appear on facebook to the ignore list if you do not want to wish these friends a happy birthday on their birthday.  
* In order to update this list with new names, navigate into the Structs folder and delete metaData.pkl 

#### wishBirthday.py

At the bottom of the file, modify the messages list as you see fit to customize your birthday messages.  Each message has an equal probability of being chosen in the first round, and then there's a 50% chance of choosing it in the second round.  The other 50% chance is to choose the birthday message "Happy Birthday first_name!".  

### Setting up an automated task (for mac users only) 
1. Navigate to ~Library/LaunchAgents/ in finder
1a. Navigate to the directory with your script and replace "YOUR_ROOTNAME_HERE" with the result from "echo $USER" command in BASH
2. paste org.lazybook.birthday.plist from your LazyBook directory into the LaunchAgents folder
3. Open up the command terminal and navigate to ~/Library/LaunchAgents
4. type "launchctl load ~/Library/LaunchAgents/org.lazybook.birthday.plist" in the terminal to load the automated task
5. Type "launchctl start org.lazybook.birthday" to start the task
6. This will wish your friends a happy birthday the moment you start the task, and then again once every 24 hours

To stop the automated task (and stop this script from running automatically), simply navigate to ~Library/LaunchAgents/ in your terminal and type "launchctl remove org.lazybook.birthday"

* [Helpful Resource for starting tasks](http://killtheyak.com/schedule-jobs-launchd/)
* [Helpful Resource for stopping tasks](http://osxdaily.com/2011/03/08/remove-an-agent-from-launchd/)

## Bugs List

* N/A so far

## TODO List

* Create a GUI!!!
* write tutorial for windows users
* create youtube tutoral for beginners
* Update getSingle function so it uses python's concurrency (like in getFriends and getBirthdays) and doesn't take 5 minutes 
* Figure out how to write a method to poke back 
* Collect posts by friends and run through a binary classifier (i.e. spam filter) to determine if a friend is "spam" or "not spam"

## License
Feel free to use this software in any legal endeavors or projects - just link back to this repo to acknowledge my work and help other developers find this script (licensed under MIT License)

## Final Thoughts

 Please don't misuse this script! It's meant to be a fun little tool to help your friends realize how much you care about them and gather analytics for personal projects.  Could you modify it to do something annoying? Yes.  Please don't be an asshole and make this a problem for Facebook so it needs to be fixed.  If you're a Facebook engineer reading this, please enjoy :)

Finally, is this legal?  Yes!  Very much so!  I sent an email to facebook's security department a while back, and they do not see it as a concern since it collects only public information.  We're not going anywhere that we're not supposed to be, and at worst, only doing something (automation) that we're not supposed to be able to automate.

If you would like to contact me to contribute or just talk, then you can reach me at cfifty.github@gmail.com.  If you enjoy using this script and would like more like it then please donate [here](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=4WHNCY5Z4GZPJ&lc=US&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted). All funds will go towards alleviating the crushing weight of student loans, my weekly coffee budget, and allowing me to work fewer hours for my university's work-study program.

