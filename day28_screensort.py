from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com")

# 1. Full page screenshot
ok = driver.save_screenshot("login_page.png")
print("Page screenshot saved:", ok)

# 2. Only one element (the logo)
logo = driver.find_element(By.CLASS_NAME, "login_logo")
logo.screenshot("logo.png")
print("Logo screenshot saved ✅")

# 3. Screenshot when a test FAILS (wrong password on purpose)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("wrong_pass")
driver.find_element(By.ID, "login-button").click()

try:
    assert "inventory" in driver.current_url, "Login failed!"
    print("Login PASS ✅")
except AssertionError as e:
    driver.save_screenshot("failed_login.png")
    print("Test FAILED:", e)
    print("Evidence saved: failed_login.png 📸")

driver.quit()