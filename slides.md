---
marp: true
theme: uncover
title: Whacky Web Bots
paginate: true
_paginate: false # skip page on first slide
---

# <!-- fit --> Whacky Web Bots

Note: Recorded for you all to be able to watch later

Email: hdeep2@illinois.edu

---

# Outline

* 1st hour - Intro and background, making a simple program to improve navigation on UIUC Course Website

* 2nd hour - Selenium and having a program control the web browser to collect data. Ending with ethical considerations and questions.

---

# Time suggestions

* For those following along async or reusing these slides (which is 100% allowed), I've added timing guides throughout the slides as well. These are just suggestions so don't worry if you're not able to finish the work in time. Especially installation stuff, that stuff can be really tricky.

---

# <!-- fit --> Intro (10 minutes)

---

# About me (general)

* I'm Harsh Deep, a junior studying Statistics and Computer Science at UIUC. hdeep2@illinois.edu

* I like teaching: I've spent 5 semesters working as CA helping teach intro CS 125.

* I also like open source, hci research (human ai teaming and eyetracking), cats, reading and watching interesting animation from around the world.

---

# Why web bots

* Almost everything is on the internet now. A gold mine of information exists which can enable us to do so many things.

* They're fun and impress people.

* Automation lets us save time, prevent errors and lets us focus on more important things.

---

# Not a gimmick 

* I used to think they were a gimmick

* then in my first tech intership I created three different bots for extracting event info and social media automation

* Not only can they make things easier in your life, they can also create business value.

---

# What do people use web browser automation for

* Testing systems automatically

* Gathering information from the internet. Mmajority of the information on the internet doesn't actually doesn't end up in an API.

* Making many poorly organized resources more accessible.

---

# <!-- fit --> Opening browsers
---  

# Setup Python (15 minutes)


- Windows: https://www.python.org/downloads/windows/ (select installer and make sure to add to path). https://phoenixnap.com/kb/how-to-install-python-3-windows - this guide is pretty useful too.
- MacOSX: https://docs.python-guide.org/starting/install3/osx/
- Linux: https://docs.python-guide.org/starting/install3/linux/

---

# Couldn't get it to work

* Don't worry. 

* This will all be recorded and the slides are all available online. 

* Ask me questions after email later too.

---

# Code Along Task (20 minutes)

* Make the UIUC Course Explorer Easier to Navigate (20 minutes)

* Problem: When you use the UIUC Course Website you can't directly jump to the Course you want

---

* Take command line input - common in real life scenario.

* Valid upper case inputs like "CS 125" or "CWL 114". 

* Code: https://github.com/harsh183/sail21-whacky-web-bots/blob/main/course_explore.py

---

# Exercise 1 (10 minutes) - Chapter goto

* Lets say we have a book that we really like named Automate The Boring Stuff with Python, but we want to jump into a chapter directly at once.

---

# Specification

* The url for each chapter has the chapter number in the end "https://automatetheboringstuff.com/2e/chapter12/" from 0 to 20 both included. 

* (Programmers have this weird obession with starting everything from 0)

* Make a program that takes the command line input `automate.py 5` and have the browser jump to the right page.

---

# JS Approach (complex)

* https://gist.github.com/harsh183/4505b4870fb9a003abe5193e0f7b9c71

* Run a custom script after the search form was filled out.

* Using JavaScript that runs directly on the Browser. Beyond scope of the class but useful.
---

# <!-- fit --> Selenium

---

# Setup Selenium (15 minutes)

If you aren't able to get this to work don't worry. This will all be recorded and the slides are all available online. I'll be open to questions after this session over email as well so feel free to ask me questions then. 

* Open your command line and type. 
   ```bash
   pip install selenium
   pip install webdriver_manager
   ```
---

# Code Along Task (20 minutes)

* Get the names of all the wonderful SAIL 2021 Organizers 

* They're an amazing set of people so perhaps we can make them all a nice thank you message.

* Final code: https://github.com/harsh183/sail21-whacky-web-bots/blob/main/sel1.py

---

# Exercise 2 (10 minutes) 

Feel free to work with others too. If your set up isn't working feel free to just discuss with others. 

* We got everyone's names out of the web page, now lets use the same logic to try to get everyone's descriptions as well.

* Use the code we've written so far as a starting point.

---

* Make sure the descriptions match up with the right people :)

* Don't worry if you aren't able get this in time, the point is to get you thinking in the right direction.

* If you aren't able to get this into code, having just a conceptual explaination is fine too. Focus on using inspect element to figure out which selectors can give the right data.

<!-- TODO: Insert link to repo with close ish example code -->

---

# Going further

* Things can get more complex.

* Instead of taking command line inputs we can have a GUI or a config file.

* More: scrolling, forms, tickets

---

# Going further

* Realistic testing: as if someone was actually using it

* You can even incorporate AI into all of this.

---

# <!-- fit --> Ethical issues 

Responsible bot development

---

# Jobs

* Automation can automate a lot of jobs. 

* [I’ve Been Replaced by an Analytics Robot](r4stats.com/2015/05/18/ive-been-replaced-by-an-analytics-robot/)

---

# Legality and court battles

* It is legal still restricted.

* Many companies oppose it while many in the public support it.

* [Web scraping is now legal](https://medium.com/@tjwaterman99/web-scraping-is-now-legal-6bf0e5730a78)

---

# Bad Actors

* Bots have the potential to be used in bad ways, for example influencing politics or harassment. [The Social Impact Of Bad Bots And What To Do About Them](https://www.forbes.com/sites/forbestechcouncil/2020/12/04/the-social-impact-of-bad-bots-and-what-to-do-about-them/?sh=4f01f7d459e0) 

---

# Covid vaccines

* People have also started using web bots to get vaccines faster. [Want a vaccination appointment? It helps to know a Python programmer](https://www.nbcnews.com/tech/security/want-vaccination-appointment-helps-know-python-programmer-rcna457)

* Innovative

* But also not everyone has access to this.

---

# Automate the Boring Stuff

* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com) - 

* free online book (with optional paid videos) that first teaches python from scratch

* second half has lots of interesting python projects in automation

* [Automate the Boring Stuff with Python Chapter 12](https://automatetheboringstuff.com/2e/chapter12/) goes into far more detail on web bot stuff. I highly reccomend.

---

# More Docs

* [Selenium Python Docs](https://selenium-python.readthedocs.io/)

* [Freecodecamp - Learn JavaScript](https://www.freecodecamp.org/)

---

# Contact

Email: hdeep2@illinois.edu
