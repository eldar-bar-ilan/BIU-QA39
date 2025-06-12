from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.maximize_window()
driver.get('http://127.0.0.1:5500/index.html')

time.sleep(1)
div3 = driver.find_element(By.ID, 'el-3')
driver.execute_script("arguments[0].scrollIntoView();", div3)

if driver.save_screenshot("./images/div3.png"):
    print("Image saved")
else:
    print("Failed to save image")

time.sleep(1)

