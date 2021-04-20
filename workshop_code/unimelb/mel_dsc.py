from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time 

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://dsc.community.dev/university-of-melbourne/")

buttons = driver.find_elements_by_class_name("chapter_section_scroll")
buttons[3].click()

name_els = driver.find_elements_by_class_name("people-card--name")
names = [el.text for el in name_els]

for i in range(len(names)):
    name = names[i]
    title = titles[i]
    print(f"Thank you {name}!")

breakpoint()