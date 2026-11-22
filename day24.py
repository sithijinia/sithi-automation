from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login(driver, username, password):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

driver = webdriver.Chrome()

# TC_003: wrong password
login(driver, "standard_user", "wrong_pass")
error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
print(error)
assert "do not match" in error, "TC_003 failed!"
print("TC_003 PASS ✅")

# TC_004: empty username
login(driver, "", "secret_sauce")
error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
print(error)
assert "Username is required" in error, "TC_004 failed!"
print("TC_004 PASS ✅")

# TC_005: empty password
login(driver,"standard_user", "")
error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
print(error)
assert "Password is required" in error, "TC_005 failed!"
print("TC_005 PASS ✅")

# TC_006: wrong username
login(driver, "wrong_user", "secret_sauce")
error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
print(error)
assert "do not match" in error, "TC_006 failed!"
print("TC_006 PASS ✅")

# TC_002: locked out user
login(driver, "locked_out_user", "secret_sauce")
error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
print(error)
assert "locked out" in error, "TC_002 failed!"
print("TC_002 PASS ✅")


# TC_001: valid login
login(driver, "standard_user", "secret_sauce")
title = driver.find_element(By.CSS_SELECTOR, "[data-test='title']").text
print(title)
assert title == "Products", "TC_001 failed!"
print("TC_001 PASS ✅")



