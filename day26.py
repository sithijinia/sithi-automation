from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_visible_text("Option 2")

selected = dropdown.first_selected_option.text
print(selected)
assert selected == "Option 2", "Wrong option selected!"
print("Dropdown test PASS ✅")

driver.get("https://the-internet.herokuapp.com/checkboxes")
boxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input")
print("Number of checkboxes:", len(boxes))

first = boxes[0]
print("Before click:", first.is_selected())
first.click()
print("After click:", first.is_selected())

assert first.is_selected() == True, "Checkbox is not selected!"
print("Checkbox test PASS ✅")
time.sleep(3)
driver.quit()