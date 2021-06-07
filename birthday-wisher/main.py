import datetime as dt
import pandas
import random
import smtplib

my_email = "notpythontest@gmail.com"
password = "kTe489XS"

now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

df = pandas.read_csv("birthdays.csv")
new_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}


def send_file():
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        conn.sendmail(
            from_addr=my_email,
            to_addrs=mail,
            msg=f"Subject:Happy birthday {name}!\n\n{contents}"
        )


if today in new_dict:
    birthday_person = new_dict[today]
    name = birthday_person["name"]
    mail = birthday_person["email"]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", name)
    send_file()
