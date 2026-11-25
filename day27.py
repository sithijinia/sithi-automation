from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# 1. Simple alert: only OK
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
print("Alert says:", alert.text)
time.sleep(2)
alert.accept()

result = driver.find_element(By.ID, "result").text
print(result)
assert result == "You successfully clicked an alert", "Alert test failed!"
print("Alert test PASS ✅")

# 2. Confirm: OK or Cancel
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
confirm = driver.switch_to.alert
print("Confirm says:", confirm.text)
time.sleep(2)
confirm.dismiss()

result = driver.find_element(By.ID, "result").text
print(result)
assert result == "You clicked: Cancel", "Confirm test failed!"
print("Confirm test PASS ✅")


# 3. Prompt: type text, then OK
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
prompt = driver.switch_to.alert
print("Prompt says:", prompt.text)
prompt.send_keys("Sithi")
time.sleep(2)
prompt.accept()

result = driver.find_element(By.ID, "result").text
print(result)
assert result == "You entered: Sithi", "Prompt test failed!"
print("Prompt test PASS ✅")
driver.quit()