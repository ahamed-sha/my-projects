from selenium import webdriver
from time import time, sleep
driver = webdriver.Chrome(executable_path="C:/Development/chromedriver.exe")

driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

timeout = time() + 5
five_min = time() + (60 * 5)

cookie = driver.find_element_by_id("cookie")
cps = driver.find_element_by_id("cps")

# Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

while True:
    cookie.click()

    if time() > timeout:
        # Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = dict(zip(item_prices, item_ids))

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, ids in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = ids

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
        if time() > five_min:
            print(cps)
            break
