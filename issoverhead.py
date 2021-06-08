import requests
from datetime import datetime
import smtplib

MY_LAT = 0
MY_LONG = 0

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def check_pos():
    if MY_LAT - 5 <= iss_longitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_dark():
    if time_now >= sunset or time_now <= sunrise:
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position
if check_pos() and is_dark():
    conn = smtplib.SMTP("smtp.gmail.com")
    conn.starttls()
    conn.login(user="test@gmail.com", password="123456789")
    conn.sendmail(
        from_addr="test@gmail.com",
        to_addrs="test@yahoo.com",
        msg="Subject:Hey vsauce\n\nLook up, ISS overhead"
    )

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


