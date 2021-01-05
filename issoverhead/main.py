import requests
from datetime import datetime
import math
import smtplib
import time

MY_LAT = 40.7127765 # Your latitude
MY_LONG = -74.005974 # Your longitude

def issOverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return math.abs(iss_latitude - MY_LAT) < 5 and math.abs(iss_longitude - MY_LONG) < 5

def isDarkOutside():
    # Your position is within +5 or -5 degrees of the ISS position.
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    return sunset <= time_now <= sunrise

while True:

    print("Checking")
    time.sleep(60)
    if isDarkOutside() and issOverhead():
        MY_EMAIL = "langzai1729@gmail.com"
        MY_PASSWORD = "6Jk6NSJ4y0CR"

        now = datetime.datetime.now()
        weekday = now.weekday()

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Look Up! \n\n The ISS is overhead right now!".encode("utf-8"))

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



