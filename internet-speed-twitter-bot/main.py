from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

PROMISED_DOWN = 100
PROMISED_UP = 50
CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"
TWITTER_EMAIL = "someone@email.com"
TWITTER_PASSWORD = "password"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = None
        self.down = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        sleep(3)
        go_button = self.driver.find_element_by_class_name("start-button")
        go_button.click()

        sleep(60)
        down_speed = self.driver.find_element_by_class_name("download-speed")
        up_speed = self.driver.find_element_by_class_name("upload-speed")

        self.up = int(up_speed.text.split(".")[0].strip())
        print(self.up)
        self.down = int(down_speed.text.split(".")[0].strip())
        print(self.down)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        sleep(3)
        username = self.driver.find_element_by_name(
            'session[username_or_email]')
        password = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')

        username.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)

        password.send_keys(Keys.ENTER)

        sleep(2)
        tweet_box = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_box.send_keys(f"Hey Internet provider, why is my internet speed is {self.down}down/{self.up}up when I am paying for {PROMISED_DOWN}down/{PROMISED_UP}up")

        tweet = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
sleep(2)
bot.tweet_at_provider()
