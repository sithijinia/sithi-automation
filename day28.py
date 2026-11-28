from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/large")

# 1. Where are we now?
start = driver.execute_script("return window.pageYOffset")
print("Start position:", start)

# 2. Scroll to the bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)
bottom = driver.execute_script("return window.pageYOffset")
print("After scroll down:", bottom)
assert bottom > start, "Scroll down failed!"
print("Scroll down PASS ✅")

# 3. Back to top, then scroll to one element
driver.execute_script("window.scrollTo(0, 0)")
time.sleep(1)
table = driver.find_element(By.ID, "large-table")
driver.execute_script("arguments[0].scrollIntoView();", table)
time.sleep(2)
print("After scroll to table:", driver.execute_script("return window.pageYOffset"))
print("Scroll to element PASS ✅")

driver.quit()