# Whacky Web Bots

## Install Python

- Windows: https://www.python.org/downloads/windows/ (select installer and make sure to add to path). https://phoenixnap.com/kb/how-to-install-python-3-windows - this guide is pretty useful too.
- MacOSX: https://docs.python-guide.org/starting/install3/osx/ or try `homebrew`
- Linux: https://docs.python-guide.org/starting/install3/linux/ or try your distro package installer
- Do `python --version` to check which you got. If it says `2.x` then you will have to use `python3 scriptname.py`

## UIUC SAIL 2021 Version

Slides for [CS Sail 21](https://sail.cs.illinois.edu/) at UIUC workshop on introducing web bots. Slides in markdown and powered by [marp](https://github.com/marp-team/marp)

Slides url: https://whacky-web-bots.netlify.app/

### Outline

Hour 1: Opening web browsers (using python stdlib `webbrowser`)
* Introduction and installation of python
* Code Along Task: Take a command line argument like `CS 125` and open the web browser to the `courses.illinois` page because the website doesn't directly let you jump to courses
* Exercise: Take a chapter number for the book Automate the Boring Stuff with Python and open directly to that webpage
Hour 2: Selenium 
* Selenium `pip` install
  - (UIUC SAIL version) Code Along Task: Open up the CS Sail homepage, click the navbar `Staff` link, hover the mouse on the `overlay` and select all staff names because we want to make them a thank you card.
  - (CS 125 version)    Code Along Task: Open up the CS 125 homepage, click the sidebar, click the people page, select all staff names because we want to make them a thank you card.
* Exercise: Get everyone's descriptions/roles as well and print it alongside.
* Ethical issues
* Closing remarks

### Dev

We use `marp` which you can install from `npm`. 

**For CS SAIL slides**

```bash
marp slides.md -o index.html
```

**For CS 125 slide**

```bash
marp 125.md -o 125.html
```