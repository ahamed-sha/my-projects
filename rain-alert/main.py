import requests
from twilio.rest import Client

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "0b99b56c4a66e27da39a6d0a1c10cec6"
account_sid = "AC85239be95f65bff30bcab4b8a73219e0"
auth_token = "78186b3bedabede606f3ecbd5d277781"

weather_params = {
    'lat': 20.145929,
    'lon': 92.876320,
    'appid': api_key,
    'exclude': 'current,daily,minutely'
}

response = requests.get(url=endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="you probably need an umbrella!",
        from_="+16149547082",
        to='+919994838033'
    )

    print(message.status)
