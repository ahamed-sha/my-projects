import smtplib
EMAIL = "test@gmail.com"
PASSWORD = "1414414"

class NotificationManager:

    def send_email(self,  message):
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=EMAIL, password=PASSWORD)
            conn.sendmail(
                from_addr=EMAIL,
                to_addrs="afaffaiyyeee",
                msg=f"Subject:Ahoy!\n\n{message}"
            )