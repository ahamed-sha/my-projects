import lxml
import requests
from bs4 import BeautifulSoup
import smtplib

PRICE = 2500
USERNAME = "hello@gmail.com"
PASSWORD = "abcde"

header = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
}

response = requests.get(
    url="https://www.amazon.in/Sony-Extra-MDR-XB450AP-Headphones-Black/dp/B00SISEOLC/ref=sr_1_16?crid=2B20YMOJXBK6J&dchild=1&keywords=sony+headphones+%E0%A4%82&qid=1624852142&sprefix=sony+head%2Caps%2C442&sr=8-16",
    headers=header
)

content = response.text

soup = BeautifulSoup(content, "lxml")
price_tag = soup.find(name="span", id="priceblock_ourprice")
price = price_tag.getText().split()[1].split(".")[0].split(",")
price = "".join(price)
price = int(price)

if price < PRICE:
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=USERNAME, password=PASSWORD)
        conn.sendmail(
            from_addr=USERNAME,
            to_addrs="hello@email.com",
            msg=f"Subject:Sony headphones price drop\n\nThe price dropped to {price}!"
        )

