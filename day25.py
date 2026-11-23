from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com")
driver.find_element(By.ID, "user-name").send_keys("performance_glitch_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait = WebDriverWait(driver, 10)
title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='title']"))).text
assert title == "Products", "Login failed!"
print("Slow user login PASS ✅")

driver.quit()