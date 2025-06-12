from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = Chrome()
driver.maximize_window()
# ===========================
driver.get('http://127.0.0.1:5500/index.html')
driver.save_screenshot('./images/img1.png')
driver.find_element(By.ID, 'first-name').send_keys('Dan')
driver.find_element(By.NAME, 'email').send_keys('dan@mail.com')
driver.find_element(By.CSS_SELECTOR, '.big').send_keys('050-12345')
driver.find_elements(By.TAG_NAME, 'input')[3].send_keys('021598745')
driver.save_screenshot('./images/img2.png')

select_element = driver.find_element(By.ID, 'color')
select = Select(select_element)
time.sleep(1)
select.select_by_index(2)
time.sleep(1)
select.select_by_value('black')
time.sleep(1)
select.select_by_visible_text('Green')
time.sleep(1)

driver.find_element(By.TAG_NAME, "button").click()
# ===========================
time.sleep(3)
driver.close()
