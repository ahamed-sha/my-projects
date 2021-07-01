from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:/Development/chromedriver.exe")

driver.get("https://www.linkedin.com/checkpoint/lg/login")

username = driver.find_element_by_id("username")
username.send_keys("oliviasanchezmex@gmail.com")

password = driver.find_element_by_id("password")
password.send_keys("Udemy123#")

login = driver.find_element_by_css_selector(".login__form_action_container button")
login.click()

sleep(2)

jobs = driver.find_element_by_id("ember25")
jobs.click()

sleep(2)

skill = driver.find_element_by_css_selector('.jobs-search-box__container .jobs-search-box__input--keyword input')
skill.send_keys("Front end developer")

location = driver.find_element_by_css_selector('.jobs-search-box__container .jobs-search-box__input--location input')
location.send_keys("ireland")

job_search = driver.find_element_by_class_name("jobs-search-box__submit-button")
job_search.click()
sleep(3)

job_cards = driver.find_elements_by_css_selector(".job-card-container--clickable")
for card in job_cards:
    print(len(job_cards))

    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "job-card-list__title")))
    driver.execute_script("arguments[0].click();", card)
    card.click()
    job_apply = driver.find_element_by_class_name("jobs-save-button")
    sleep(1)
    job_apply.click()
