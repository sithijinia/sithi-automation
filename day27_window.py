from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://the-internet.herokuapp.com/windows")

# 1. Remember the original tab
original = driver.current_window_handle

# 2. Click link -> new tab opens
driver.find_element(By.LINK_TEXT, "Click Here").click()
wait.until(EC.number_of_windows_to_be(2))
print("Total tabs:", len(driver.window_handles))

# 3. Switch to the NEW tab
for handle in driver.window_handles:
    if handle != original:
        driver.switch_to.window(handle)

new_heading = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3"))).text
print("New tab:", new_heading)
assert new_heading == "New Window", "New tab test failed!"
print("New tab test PASS ✅")

# 4. Close new tab, go back to original
driver.close()
driver.switch_to.window(original)
old_heading = driver.find_element(By.TAG_NAME, "h3").text
print("Original tab:", old_heading)
assert old_heading == "Opening a new window", "Original tab test failed!"
print("Original tab test PASS ✅")

driver.quit()