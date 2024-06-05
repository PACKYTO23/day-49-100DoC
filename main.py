from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "..."
PASSWORD = "..."

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://mx.linkedin.com/")

# sign_in_with_email = driver.find_element(By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/a')
email_or_phone = driver.find_element(By.ID, value="session_key")
password = driver.find_element(By.ID, value="session_password")

# time.sleep(5)
# sign_in_with_email.send_keys(Keys.ENTER)
time.sleep(5)
email_or_phone.send_keys(EMAIL)
time.sleep(3)
password.send_keys(PASSWORD, Keys.ENTER)
