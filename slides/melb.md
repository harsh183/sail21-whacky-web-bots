---
marp: true
theme: uncover
title: Wacky Web Bots
paginate: true
_paginate: false # skip page on first slide
---

# <!-- fit --> Wacky Web Bots

Note: Recorded for you all to be able to watch later

Email: hdeep2@illinois.edu

---

# Outline

* `webbrowser` built in library to navigate to course pages and book chapters

* `selenium` to scrape DSC information

---

# Time Suggestions

* For those following along async or reusing these slides (which is 100% allowed), I've added timing guides throughout the slides as well. These are just suggestions so don't worry if you're not able to finish the work in time. Especially installation stuff, that stuff can be really tricky.

---

# <!-- fit --> Intro (5 minutes)

---

# Why Web Bots

* Almost everything is on the internet now. A gold mine of information exists which can enable us to do so many things.

* They're fun and impress people.

* Automation lets us save time, prevent errors and create business value.

---


# Uses

* Testing systems automatically

* Gathering information from the internet. Most of the internet is not on an API.

* Making many poorly organized resources more accessible.

---

# <!-- fit --> Opening Browsers
---  

# Setup (10 minutes)

- Windows: https://www.python.org/downloads/windows/ (select installer and make sure to add to path). https://phoenixnap.com/kb/how-to-install-python-3-windows - this guide is pretty useful too.
- MacOSX: https://docs.python-guide.org/starting/install3/osx/
- Linux: https://docs.python-guide.org/starting/install3/linux/
- Do `python --version` to check. If it says `2.x` then run code with `python3 scriptname.py`


---

# Setup Selenium

If you aren't able to get this to work don't worry. This will all be recorded and the slides are all available online. I'll be open to questions after this session over email as well so feel free to ask me questions then. 

* Open your command line and type. Do `pip3` instead if you have been using `python3` so far.
   ```bash
   pip install selenium
   pip install webdriver_manager
   ```
---

# Couldn't Get It To Work

* Don't worry. 

* This will all be recorded and the slides are all available online. 

* Ask me questions after email later too.

---

# Code Along Task (10 minutes)

* Make the University Course Explorer Easier to Navigate

* Problem: When you use the Handbook Course Website you can't directly jump to the Course you want

---

* Take command line input - common in real life scenario.

* Valid upper case inputs like "COMP30027" or "COMP10001". 

* [Code](https://github.com/harsh183/sail21-whacky-web-bots/blob/main/workshop_code/unimelb/handbook_mel.py)

---

# Approach

* Figure out `base_url`

* Construct new url `base_url + extention` based on input

* Use `webbrowser.open()`

---

# Exercise 1 (5 minutes) - Chapter goto

* We want to jump to chapters of Automate The Boring Stuff with Python

* The url for each chapter has the chapter number in the end "https://automatetheboringstuff.com/2e/chapter12/" from 0 to 20 both included. 

* Command line input `automate.py 5` 

---

# <!-- fit --> Selenium

---

# Code Along Task (15 minutes)

* Get the names of all the wonderful DSC Staff 

* https://dsc.community.dev/university-of-melbourne/

* They're an amazing set of people so perhaps we can make them all a nice thank you message.

---

# Approach

* Inspect element to find a pattern

* Figure out how to match that pattern on selenium

* Perform an action on selected element (click, read, hover, fill) and repeat this cycle

---

# Exercise 2 (5 minutes) 

* Feel free to work with others too. If your set up isn't working feel free to just discuss with others. 

* We got everyone's names out of the web page, now lets use the same logic to try to get everyone's roles as well.

* Previous [code](https://github.com/harsh183/sail21-whacky-web-bots/blob/main/workshop_code/unimelb/mel_dsc.py)

---

# Going Further

* Things can get more complex.

* Instead of taking command line inputs we can have a GUI or a config file.

* More: scrolling, forms, tickets

---

# Going Further

* Test frameworks

* You can even incorporate AI into all of this.

---

# <!-- fit --> Ethical issues 

Responsible bot development

---

# Jobs

* Automation can automate a lot of jobs. 

* [I???ve Been Replaced by an Analytics Robot](r4stats.com/2015/05/18/ive-been-replaced-by-an-analytics-robot/)

---

# Legality and Court Battles

* It is legal but still restricted.

* Many companies oppose it while many in the public support it.

* [Web scraping is now legal](https://medium.com/@tjwaterman99/web-scraping-is-now-legal-6bf0e5730a78)

---

# Bad Actors

* Bots have the potential to be used in bad ways, for example influencing politics or harassment. [The Social Impact Of Bad Bots And What To Do About Them](https://www.forbes.com/sites/forbestechcouncil/2020/12/04/the-social-impact-of-bad-bots-and-what-to-do-about-them/?sh=4f01f7d459e0) 

---

# Covid Vaccines

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

Code: https://github.com/harsh183/sail21-whacky-web-bots/