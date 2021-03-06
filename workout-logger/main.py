from datetime import datetime
import os
import requests

API_KEY = "f4f5a0d6f651d89de5be2185c7e24187"
APP_ID = "83095ef5"
USER_ID = "0"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT_KG = 65.5
HEIGHT_CM = 173
AGE = 18
exercise_text = input("What was your workout?\n")

sheet_endpoint = "https://api.sheety.co/417e5053abd8264717dd8a4b428d2c86/myWorkouts/workouts"


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
requests.get('https://api.github.com/user', auth=('user', 'pass'))
################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
bearer_headers = {"Authorization": "abc123"}
username = "username"
password = "password"
basic_auth = (username, password)
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    # sheet_respones = requests.post(sheet_endpoint, json=sheet_inputs, headers = bearer_headers)
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=basic_auth)

    print(sheet_response.text)