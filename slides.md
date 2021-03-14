-- 
marp: true
theme: uncover
---

# <!-- fit --> Whacky Web Bots

---

# Outline

* 1st hour - Intro and background, making a simple program to improve navigation on UIUC Course Website

* 2nd hour - Selenium and having a program control the web browser to collect data.

---

# About me (general)

* I'm Harsh Deep, a junior studying Statistics and Computer Science at UIUC.

* I've spent 5 semesters working as CA helping teach intro CS 125 and generally like teaching and helping people on just about anything.

* I also have spent many semesters working with professors and grad students in HCI around eye tracking. I've also spent a while working on various open source projects on [Github](https://github.com/harsh183/)

* Outside school I like reading, cats, and thinking critically about a lot of animated content from various countries.

* If you want to ask me questsions about any of this stuff after class feel free as well.

---

# Why web bots

* Almost everything is on the internet now. A gold mine of information exists which can enable us to do so many things.

* They're fun and impress people.

* Automation lets us save time, prevent errors and lets us focus on more important things.

* I used to think they were a gimmick, but then in my first tech intership I created three different bots for extracting event info and social media automation and realized how much it could aid marketing and sales processes at companies.

---

# What do people use web browser automation for

* Testing systems automatically - at some point it's simply not possible for a large company to retest thousands of pages manually every time someone makes a change.

* Gathering information from the internet. Commonly known as Web Scraping. Lots of times companies make special APIs for programmers to access but the majority of the information on the internet doesn't actually doesn't end up in an API.

* 

---

# <!-- fit --> Web Automation

Making Life Simpler

---  

# Code Along Task: Make the UIUC Course Explorer Easier to Navigate (20 minutes)

* Problem: When you use the UIUC Course Website you can't directly jump to the Course you want

* Instead: Let's have a bot take an Input from us and then use that information to navigate to the right task.

* We're not going to worry about invalid inputs, just something like `CS 125` or `CWL 114`.

---

# Another more complex approach with JS to the Course Explorer Problem

* https://gist.github.com/harsh183/4505b4870fb9a003abe5193e0f7b9c71

* In my freshman year I approached this problem another way by using `JavaScript` to run a custom script after the search form was filled out.

* I split up the input into Name and Number and then figured out what URL to let people directly jump to. 

* This is only possible with a language called JavaScript that runs directly on the Browser. This is beyond the scope of this 2 hour class to cover another language but if you want to learn more about web browser automation learning [JavaScript](https://www.freecodecamp.org/) is worth it.

---

# <!-- fit --> Scraping

Extracting data

---

# Setup Selenium(20 minutes)

If you aren't able to get this to work don't worry. This will all be recorded and the slides are all available online. I'll be open to questions after this session over email as well so feel free to ask me questions then. 

1. Open your command line and type. 
   ```bash
   pip install selenium
   ```

2. Download the webdrivers for [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads). You can do this with any web browser of choice but using Chrome makes life simpler.

3. Follow instructions on [here](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/) to set up the Chrome drivers right for your specific OS. If you want to use another web browser this page also has instructions for that.


---

# Code Along Task: Get the names of all the wonderful SAIL 2021 Organizers (20 minutes)

* They're an amazing set of people so perhaps we can make them all a nice thank you message.

* Normally what you'd do is just copy paste their names into a card and the just move on with your lives, but here we use a computer that can operate a web browser for it.

* This can scale even if we have 90 or even 900,000 organizers on one team. That's one of the nice things about computers, they're really good at handling volume.


# Exercise 2: 20 minutes 

Feel free to work with others too. If your set up isn't working feel free to just discuss with others. 

* We got everyone's names out of the web page, now lets use the same logic to try to get everyone's descriptions as well.

* Use the code we've written so far as a starting point.

* Make sure the descriptions match up with the right people :)

* Don't worry if you aren't able get this in time, the point is to get you thinking in the right direction.

* If you aren't able to get this into code, having just a conceptual explaination is fine too. Focus on using inspect element to figure out which selectors can give the right data.

<!-- TODO: Insert link to repo with close ish example code -->

---

# Ethical issues and links to some articles to learn more

These are only the tip of the iceberg, but we should be responsible while developing automated tools considering our impact on society.

* Automation can automate a lot of jobs. [I’ve Been Replaced by an Analytics Robot](r4stats.com/2015/05/18/ive-been-replaced-by-an-analytics-robot/)

* It is legal now after being in a gray area for a while, but still faces restrictions in many categories. [Web scraping is now legal](https://medium.com/@tjwaterman99/web-scraping-is-now-legal-6bf0e5730a78)

* Bots have the potential to be used in bad ways, for example influencing politics or harassment. [The Social Impact Of Bad Bots And What To Do About Them](https://www.forbes.com/sites/forbestechcouncil/2020/12/04/the-social-impact-of-bad-bots-and-what-to-do-about-them/?sh=4f01f7d459e0) 

---

# More Resources:

* [Automate the Boring Stuff with Python Chapter 12](https://automatetheboringstuff.com/2e/chapter12/) - this chapter goes over a lot more and in general this book is my goto for taking people who know nothing about programming to making useful personal projects that can also be useful in many lines of work.

* [Selenium Python Docs](https://selenium-python.readthedocs.io/)

* [Freecodecamp - Learn JavaScript](https://www.freecodecamp.org/)