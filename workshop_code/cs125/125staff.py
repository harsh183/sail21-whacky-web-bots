from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time 

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://cs125.cs.illinois.edu/")

buttons = driver.find_elements_by_class_name("MuiButtonBase-root")
buttons[1].click()
time.sleep(2)

menu_items = driver.find_elements_by_class_name("MuiListItem-root")
menu_items[5].click()

time.sleep(5) # let things load
name_tags = driver.find_elements_by_class_name("MuiTypography-h4")
names = [n.text for n in name_tags][5:]
print(names)

# Exercise: Get people's roles as well

breakpoint()