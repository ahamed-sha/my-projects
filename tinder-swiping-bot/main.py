from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome(executable_path="C:/Development/chromedriver.exe")

driver.get("https://tinder.com/")

sleep(2)
login_button = driver.find_element_by_class_name('button')
login_button.click()

sleep(2)
try:
    login_with_fb = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
    login_with_fb.click()

except NoSuchElementException:
    more_options = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div[1]/div/div[3]/span/button')
    more_options.click()
    sleep(1)
    login_with_fb = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
    login_with_fb.click()

sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

facebook_email = driver.find_element_by_css_selector(".clearfix #email")
facebook_email.send_keys("someone@email.com")

facebook_pass = driver.find_element_by_css_selector(".clearfix #pass")
facebook_pass.send_keys("password")

fb_login_button = driver.find_element_by_name("login")
fb_login_button.click()

sleep(5)

driver.switch_to.window(base_window)
try:
    cookies = driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[2]/div/div/div[1]/button')
    cookies.click()

    sleep(1)
    allow = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div/div/div[3]/button[1]')
    allow.click()

    sleep(1)
    notifs = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div/div/div[3]/button[2]')
    notifs.click()

except NoSuchElementException:
    allow = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div/div/div[3]/button[1]')
    allow.click()

    sleep(1)
    notifs = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div/div/div[3]/button[2]')
    notifs.click()

sleep(10)
for n in range(50):
    try:
        like_button = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        driver.execute_script("arguments[0].click();", like_button)
        sleep(2)
    except NoSuchElementException:
        sleep(2)

driver.quit()
# /html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button
# //*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button
# /html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button
