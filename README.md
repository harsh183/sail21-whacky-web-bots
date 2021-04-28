# Wacky Web Bots Workshop

Learn about embracing the power of web browsers, all powered by the magic of Python. In this workshop, you will learn about using `webbrowser` and `selenium` to take control of your web browser via Python commands. Web automation is useful for automated testing, scraping data, getting concert tickets, filling in tedious forms or just making your life easier. This is also a helpful skill in the industry where small automation scripts can generate lots of business value, like automating tedious jobs or generating leads. Plus, it's flashy and fun to show to people :)

 CC0-1.0 License - aka reuse it for whatever. If you do use it I'd like to see it though :)
 
## Setup

Follow these two steps before the workshop. There is some time at the start to sort out some issues but it's better to come prepared.

### Install Python3

- Windows: https://www.python.org/downloads/windows/ (select installer and make sure to add to path). https://phoenixnap.com/kb/how-to-install-python-3-windows - this guide is pretty useful too.
- MacOSX: https://docs.python-guide.org/starting/install3/osx/ or try `homebrew`
- Linux: https://docs.python-guide.org/starting/install3/linux/ or try your distro package installer
- Do `python --version` to check which you got. If it says `2.x` then you will have to use `python3 scriptname.py`

### Install Selenium

If you did `python3` earlier instead of `python` here you will have to use `pip3` instead of `pip`.

```bash
pip install selenium
pip install webdriver_manager
```

## University of Melbourne DSC Version

Slides are [here](https://whacky-web-bots.netlify.app/dist/melb.html) and the programs are [here](https://github.com/harsh183/sail21-whacky-web-bots/tree/main/workshop_code/unimelb).

## CS 125 Version

Slides are [here](https://whacky-web-bots.netlify.app/dist/125.html) and the programs are [here](https://github.com/harsh183/sail21-whacky-web-bots/tree/main/workshop_code/cs125).

## UIUC SAIL 2021 Version

Slides are [here](https://whacky-web-bots.netlify.app/dist/sail.html) and the programs are the programs are [here](https://github.com/harsh183/sail21-whacky-web-bots/tree/main/workshop_code/sail21).

## Outline

### Opening web browsers 

(using python stdlib `webbrowser`)
* Introduction and installation of python
* Code Along Task: Take a command line argument like `CS 125` and open the web browser to the university course explorer page.
* Exercise: Take a chapter number for the book Automate the Boring Stuff with Python and open directly to that webpage

### Selenium 

* Selenium `pip` install
  - (UIUC SAIL version) Code Along Task: Open up the CS Sail homepage, click the navbar `Staff` link, hover the mouse on the `overlay` and select all staff names because we want to make them a thank you card.
  - (CS 125 version)    Code Along Task: Open up the CS 125 homepage, click the sidebar, click the people page, select all staff names because we want to make them a thank you card.
  - (Unimelb Version) Code Along Task: Open up the DSC organizers page, click the `Organizers Link`, select all the staff names because we want to make them a thank you card.
* Exercise: Get everyone's descriptions/roles as well and print it alongside.
* Ethical issues
* Closing remarks

Note: Time adjusted to 1/2 hours as needed.

## Dev

Slides in markdown and powered by [marp](https://github.com/marp-team/marp).

Originally made for UIUC [CS Sail 21](https://sail.cs.illinois.edu/).

Just write the slides and commit. Github actions takes care of the rest via `marp-action`. 

For local compile, we use `marp` which you can install from `npm`.

```bash
$ marp -I slides/ --output dist/
```
