# CC0 1.0 Universal - Harsh Deep
# This program takes gets the names and roles of all the unimelb DSC team members

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time 

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://dsc.community.dev/university-of-melbourne/")

buttons = driver.find_elements_by_class_name("chapter_section_scroll")
buttons[3].click()

name_els = driver.find_elements_by_class_name("people-card--name")
names = [el.text for el in name_els]

title_els = driver.find_elements_by_class_name("people-card--title")
titles = [el.text for el in title_els]

for i in range(len(names)):
    name = names[i]
    title = titles[i]
    print(f"Thank you {name} your work in {title}!")

breakpoint()