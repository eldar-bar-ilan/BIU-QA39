from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.maximize_window()
driver.get('http://127.0.0.1:5000')

time.sleep(2)
# find and click the delete button
driver.find_element(By.XPATH, '//*[@id="product-table"]/tr/td[5]/button[3]').click()
# switch to popup widow
confirm_popup = driver.switch_to.alert
time.sleep(2)

# dismiss
# confirm_popup.dismiss()

# confirm
confirm_popup.accept()

time.sleep(3)
driver.close()
