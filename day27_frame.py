from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/nested_frames")

# 1. Go into TOP frame, then into MIDDLE frame
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-middle")
middle_text = driver.find_element(By.ID, "content").text
print("Middle frame:", middle_text)
assert middle_text == "MIDDLE", "Middle frame test failed!"
print("Middle frame test PASS ✅")

# 2. Come back OUT, then go into BOTTOM frame
driver.switch_to.default_content()
driver.switch_to.frame("frame-bottom")
bottom_text = driver.find_element(By.TAG_NAME, "body").text
print("Bottom frame:", bottom_text)
assert bottom_text == "BOTTOM", "Bottom frame test failed!"
print("Bottom frame test PASS ✅")

driver.switch_to.default_content()
driver.quit()