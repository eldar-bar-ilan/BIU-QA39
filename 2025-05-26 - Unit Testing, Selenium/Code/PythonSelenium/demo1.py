# to operate a browser from Python we need a WebDeriver object
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

# open Chrome browser
driver = Chrome()
time.sleep(2)
# navigate to a url
driver.get("http://localhost:5500/index.html")
time.sleep(2)

# finding elements
# find the input field and send text to it
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("Eldar")
time.sleep(30)

