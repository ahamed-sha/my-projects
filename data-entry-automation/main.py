from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from time import sleep

CHROME_PATH = "C:/Development/chromedriver.exe"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdNHeDepFra9atn97Bya7JNQj387Ej6DjTjWxlDwxxmlHLg/viewform?usp=sf_link"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.70318068457031%2C%22east%22%3A-122.16347731542969%2C%22south%22%3A37.66421828296719%2C%22north%22%3A37.88619799953031%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
ZILLOW = "www.zillow.com"
# ----------------------- BEAUTIFULSOUP PARSER / ZILLOW ----------------------- #


while True:
    header = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    }

    response = requests.get(url=ZILLOW_URL, headers=header)
    website_html = response.text

    soup = BeautifulSoup(website_html, "html.parser")
    price_tags = soup.select(".list-card-heading")

    price_list = []
    for tag in price_tags[0:-1]:
        try:
            price = tag.select(".list-card-price")[0].contents[0]
        except IndexError:
            # Price with multiple listings
            price = tag.select(".list-card-details li")[0].contents[0]
        finally:
            price_list.append(str(price))
    if "</abbr>" in price_list[0].split("."):
        continue
    else:
        break
print("price", len(price_list))
# Address
address_list = []
address_tags = soup.find_all(name="address")
for address in address_tags:
    address_list.append(address.contents[0])
print("add", len(address_list))
# Links
link_list = []
all_anchor_tags = soup.find_all(name="a", class_="list-card-link")
for tag in all_anchor_tags[::2]:
    tag = tag.get("href")
    if ZILLOW not in tag.split("/"):
        tag = f"https://{ZILLOW}" + tag
    link_list.append(tag)
print("link", len(link_list))

# ----------------------- SELENIUM / GOOGLE FORM ----------------------- #

driver = webdriver.Chrome(executable_path=CHROME_PATH)
driver.get(FORM_URL)
sleep(1)

count = 0
for i in range(len(price_list)):

    add_element = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_element.send_keys(address_list[count])
    sleep(1)

    price_element = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_element.send_keys(price_list[count])
    sleep(1)

    link_element = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_element.send_keys(link_list[count])
    sleep(1)

    count += 1

    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit_button.click()
    sleep(1)

    another_response = driver.find_element_by_link_text("Submit another response")
    another_response.click()

driver.quit()
