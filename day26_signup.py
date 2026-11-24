from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

driver.find_element(By.ID, "my-text-id").send_keys("Sithi")
driver.find_element(By.NAME, "my-password").send_keys("Test@1234")
Select(driver.find_element(By.NAME, "my-select")).select_by_visible_text("Two")

driver.find_element(By.ID, "my-check-2").click()
driver.find_element(By.ID, "my-radio-2").click()

print("Checkbox 2:", driver.find_element(By.ID, "my-check-2").is_selected())
print("Radio 2:", driver.find_element(By.ID, "my-radio-2").is_selected())
print("Radio 1:", driver.find_element(By.ID, "my-radio-1").is_selected())

time.sleep(10)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

message = driver.find_element(By.ID, "message").text
print(message)
assert message == "Received!", "Form was not submitted!"
print("Web form test PASS ✅")

driver.quit()