import smtplib
EMAIL = "test@gmail.com"
PASSWORD = "1234567"

class NotificationManager:

    def send_emails(self,  emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=EMAIL, password=PASSWORD)
            for email in emails:
                conn.sendmail(
                    from_addr=EMAIL,
                    to_addrs=email,
                    msg=f"Subject:Ahoy!\n\n{message}\n{google_flight_link}"
                )
