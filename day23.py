from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

username = driver.find_element(By.ID, "user-name")
username.send_keys("wrong_user")
time.sleep(2)
username.clear()
username.send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

title = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
assert title.text == "Products", "Title is wrong!"
print("TC_001 PASS ✅")

time.sleep(3)
driver.quit()