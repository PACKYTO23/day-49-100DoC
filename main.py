from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = ...
PASSWORD = ...

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://mx.linkedin.com/")

time.sleep(2.5)
sign_in = driver.find_element(By.LINK_TEXT, value="Inicia sesión")
sign_in.click()

time.sleep(2.5)
email_or_phone = driver.find_element(By.ID, value="username")
email_or_phone.send_keys(EMAIL)

time.sleep(1)
password = driver.find_element(By.ID, value="password")
password.send_keys(PASSWORD, Keys.ENTER)

time.sleep(3)
search = driver.find_element(By.XPATH, value='//*[@id="global-nav-typeahead"]/input')
search.send_keys("python trainee", Keys.ENTER)

time.sleep(2)
mx_search = driver.find_element(By.LINK_TEXT, value="Ver todos los resultados en Mexico")
mx_search.click()

time.sleep(3)
job_listings = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")

time.sleep(3)
positive_profile = driver.find_element(By.CLASS_NAME, value="job-card-container__job-insight-text")

for job in job_listings:
    if positive_profile.text == "Tu perfil se ajusta a este empleo":
        print(f"{job.text}, HAS JOB OPPORTUNITY!")
        time.sleep(1)
