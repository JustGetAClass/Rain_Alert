import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv("C:/Users/Moham/PycharmProjects/Environment_Variables/.env")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
api_key = os.getenv("api_key")
personal_phone_no = os.getenv("personal_phone_no")

client = Client(account_sid, auth_token)

parameters = {
    "lat": -5.042495,               # lat and long from somewhere in Tabora,TZ where it is raining
    "lon": 32.819733,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"][:12]  # selects 12 hours


def is_it_raining():
    for hourly_data in weather_data:
        if hourly_data["weather"][0]["id"] < 700:
            return True


def send_sms(rain):
    if rain:
        message = client.messages \
                        .create(
                             body="It is going to rain today bring an Umbrella.☔",
                             from_='+13393310995',
                             to=personal_phone_no
                         )
        # print(message.sid)
        print(message.status)


send_sms(is_it_raining())
