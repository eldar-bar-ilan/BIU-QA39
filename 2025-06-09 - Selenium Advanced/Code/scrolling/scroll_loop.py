from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.maximize_window()
driver.get('http://127.0.0.1:5500/index.html')


for i in range(1, 6):
    div = driver.find_element(By.ID, f'el-{i}')
    driver.execute_script("arguments[0].scrollIntoView();", div)
    time.sleep(1)
    driver.save_screenshot(f'./images/div-{i}.png')
