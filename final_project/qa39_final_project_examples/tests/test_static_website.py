from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.maximize_window()
driver.get('http://127.0.0.1:5000/other/home')

# click this button to get a prompt popup window
driver.find_element(By.XPATH, '/html/body/section/main/button[1]').click()
time.sleep(2)

# switch the focus to the popup window
prompt = driver.switch_to.alert
# send text to the prompt
prompt.send_keys('This is cool!')
# click ok to approve
prompt.accept()


time.sleep(10)
driver.close()

