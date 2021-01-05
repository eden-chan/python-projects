from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/417e5053abd8264717dd8a4b428d2c86/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/417e5053abd8264717dd8a4b428d2c86/flightDeals/users"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def join_mailing_list(self):
        print(f"Welcome to Eden's Flight Club.\n"
              f" We find the best flight deals and email you.")
        fname = input("What is your first name?\n")
        lname = input("What is your last name?\n")
        email = input("What is your email?\n")
        email_2 = input("Type your email again.\n")
        if email == email_2:
            print("You're in the club!")
            response = requests.get(url=SHEETY_USERS_ENDPOINT)
            print(response.json())
            user_info = {
                "user": {
                    'firstName':fname,
                    'lastName':lname,
                    'email':email,
                }
            }
            response = requests.post(
                url=SHEETY_USERS_ENDPOINT,
            json = user_info)
