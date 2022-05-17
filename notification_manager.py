import os
import smtplib

from twilio.rest import Client

TWILIO_SID = "AC1eccdbe53e16f3d57848a451fca1da54"
TWILIO_AUTH_TOKEN = os.getenv("MY TWILIO AUTH TOKEN")
TWILIO_VIRTUAL_NUMBER = os.getenv("MY TWILIO VIRTUAL NUMBER")
TWILIO_VERIFIED_NUMBER = os.getenv("MY TWILIO VERIFIED NUMBER")
MY_EMAIL = "astonleonardlo22@gmail.com"
MY_PASSWORD = os.getenv("Email Password")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, messages):
        messages = self.client.messages.create(
            body=messages,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(messages.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
