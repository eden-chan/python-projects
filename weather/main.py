import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient



API_KEY = "fc6d825cb3db43f8fdcf75b8d5bb2bf5"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_LATITUDE = 43.774582
MY_LONGITUDE = -79.25236
DES_MOINES_LATITUDE = 41.58976
DES_MOINES_LONGITUDE = -93.61565
PRECIPTATION_UPPERBOUND_ID = 700
TWILIO_AUTH_TOKEN = "bf72c5f05c07f8ed53d90d02ebf2be61"
TWILIO_ACCOUNT_SID = "AC6380bdd9461307da170e0f401b21c480"

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY,
    "exclude": "current, minutely, daily"

}
response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"]
will_rain = False
for hourly_forecast in weather_data[0:12]:

    if hourly_forecast["weather"][0]["id"] < PRECIPTATION_UPPERBOUND_ID:
        will_rain = True

# if will_rain:
#     from twilio.rest import Client
#     from twilio.http.http_client import TwilioHttpClient
#     TWILIO_AUTH_TOKEN = "bf72c5f05c07f8ed53d90d02ebf2be61"
#     TWILIO_ACCOUNT_SID = "AC6380bdd9461307da170e0f401b21c480"
#     proxy_client = TwilioHttpClient()
#     proxy_client.session.proxies = {'https': os.environ['https_proxy']}
#     account_sid = TWILIO_ACCOUNT_SID
#     auth_token = TWILIO_AUTH_TOKEN
#     client = Client(account_sid, auth_token, http_client=proxy_client)
#
#     message = client.messages.create(
#                          body="It's going to rain today. Bring an umbrella ☂️",
#                          from_='+19382385586',
#                          to='+1 647-766-2052'
#                      )
#
#     print(message.status)
