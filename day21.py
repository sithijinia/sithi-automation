from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
time.sleep(2)

product = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
print(product.text)

product = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bike Light']")
print(product.text)

product = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']")
print(product.text)

product = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Fleece Jacket']")
print(product.text)

time.sleep(5)
driver.quit()