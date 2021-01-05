import requests

MY_LAT = 43.653225
MY_LONG = -79.383186

parameters = {
    "lat": MY_LAT,
    "lng":MY_LONG,
    "formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()


data = response.json()["results"]
sunset_time = data["sunset"].split("T")[1][0:8]
sunrise_time = data["sunrise"]
sunset_formatted_time = sunset_time.split("T")[1][0:8]
sunrise_formatted_time = sunrise_time.split("T")[1][0:8]

print(sunset)