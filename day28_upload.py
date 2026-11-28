from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/upload")

# 1. Get the full path of the file
file_path = os.path.abspath("logo.png")
print("Uploading:", file_path)

# 2. Send the path to the file input (no Mac window needed!)
upload = driver.find_element(By.ID, "file-upload")
upload.send_keys(file_path)

# 3. Click Upload
driver.find_element(By.ID, "file-submit").click()

# 4. Verify
heading = driver.find_element(By.TAG_NAME, "h3").text
uploaded = driver.find_element(By.ID, "uploaded-files").text
print(heading)
print("Uploaded file:", uploaded)
assert heading == "File Uploaded!", "Upload failed!"
assert uploaded == "logo.png", "Wrong file name!"
print("Upload test PASS ✅")

driver.quit()