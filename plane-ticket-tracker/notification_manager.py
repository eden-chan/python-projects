import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from flight_data import FlightData

TWILIO_AUTH_TOKEN = "bf72c5f05c07f8ed53d90d02ebf2be61"
TWILIO_ACCOUNT_SID = "AC6380bdd9461307da170e0f401b21c480"


class NotificationManager:
    def notify(self,flight:FlightData):
        # proxy_client = TwilioHttpClient()
        # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        # client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        body_message = f"Low Price Alert! Only ${flight.price} to fly from "
                 f"{flight.origin_city}-{flight.origin_airport} to {flight.destination_airport}"
                 f"{flight.destination_airport} from {flight.out_date} to {flight.return_date}"
        message = client.messages.create(
            body = body_message
            from_='+19382385586',
            to='+1 647-766-2052'
        )
        print(message.status)

