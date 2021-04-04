# Whacky Web Bots Workshop

Slides in markdown and powered by [marp](https://github.com/marp-team/marp).

Originally made for UIUC [CS Sail 21](https://sail.cs.illinois.edu/).

 CC0-1.0 License - aka reuse it for whatever. If you do use it I'd like to see it though :)

## Install Python

- Windows: https://www.python.org/downloads/windows/ (select installer and make sure to add to path). https://phoenixnap.com/kb/how-to-install-python-3-windows - this guide is pretty useful too.
- MacOSX: https://docs.python-guide.org/starting/install3/osx/ or try `homebrew`
- Linux: https://docs.python-guide.org/starting/install3/linux/ or try your distro package installer
- Do `python --version` to check which you got. If it says `2.x` then you will have to use `python3 scriptname.py`

## CS 125 Version

Slides are [here](https://whacky-web-bots.netlify.app/125.html) and the programs are in this repo as [course_explore.py](https://github.com/harsh183/sail21-whacky-web-bots/blob/main/course_explore.py), [book.py](https://github.com/harsh183/sail21-whacky-web-bots/blob/main/book.py), and [125staff.py](https://github.com/harsh183/sail21-whacky-web-bots/blob/main/125staff.py).

## UIUC SAIL 2021 Version

Slides are [here](https://whacky-web-bots.netlify.app/) and the programs are in this repo as [course_explore.py](https://github.com/harsh183/sail21-whacky-web-bots/blob/main/course_explore.py), [book.py](https://github.com/harsh183/sail21-whacky-web-bots/blob/main/book.py), and [sel1.py](https://github.com/harsh183/sail21-whacky-web-bots/blob/main/sel1.py).

## Outline

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

## Dev

We use `marp` which you can install from `npm`. 

**For CS SAIL slides**

```bash
marp slides.md -o index.html
```

**For CS 125 slide**

```bash
marp 125.md -o 125.html
```
