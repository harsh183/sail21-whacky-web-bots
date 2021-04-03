from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://sail.cs.illinois.edu/")

nav_links = driver.find_elements_by_class_name("nav-link")
nav_links[2].click()

first_staff = driver.find_elements_by_class_name("overlay")[0]
ActionChains(driver).move_to_element(first_staff).perform()

name_elements = driver.find_elements_by_class_name("name")
staff_names = [name_el.text for name_el in name_elements] 
print(staff_names)

# Exercise
des_elements = driver.find_elements_by_class_name("text")
staff_descriptions = [des_el.text for des_el in des_elements] 
print(staff_descriptions)

breakpoint()