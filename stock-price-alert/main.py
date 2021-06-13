import smtplib
import requests
from datetime import datetime, timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
EMAIL = "test@gmail.com"
PASSWORD = "abcdefgh123#"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "013u018222"
STOCK_API_KEY = "9242817204820"

stock_params = {
    "apikey": STOCK_API_KEY,
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "outputsize": "compact"
}

news_params = {
    "q": "tesla",
    "apiKey": NEWS_API_KEY
}

yesterday = datetime.now() - timedelta(1)
yesterday = datetime.strftime(yesterday, '%Y-%m-%d')
previous_day = datetime.now() - timedelta(2)
previous_day = datetime.strftime(previous_day, '%Y-%m-%d')

# stock_value
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_price = response.json()
yesterday_price = float(stock_price["Time Series (Daily)"][yesterday]["4. close"])
previous_day_price = float(stock_price["Time Series (Daily)"][previous_day]["4. close"])

# percentage of difference between yesterday's and day before yesterday's
difference = yesterday_price - previous_day_price
if difference > 0:
    fall_rise = "value decreased to"
else:
    fall_rise = "value increased to"
abs_difference = abs(difference)
denominator = (yesterday_price + previous_day_price) / 2
percentage = round((abs_difference * 100) / denominator, 2)

if percentage > 5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    top_news = news_response.json()
    total_news = 3
    list_of_news = []
    for news_num in range(total_news):
        list_of_news.append(top_news["articles"][news_num]["title"])

        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=EMAIL, password=PASSWORD)
            conn.sendmail(
                from_addr=EMAIL,
                to_addrs="test2@gmail.com",
                msg=f"Subject:Tesla {fall_rise} {percentage}%\n\n{list_of_news[news_num]}"
            )
