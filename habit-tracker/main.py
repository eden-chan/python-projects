from datetime import datetime

import requests
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "9guaeohcru1390age"
MY_USERNAME = "eden-chan717"
user_params = {
    "token": TOKEN,
    "username": MY_USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# response.raise_for_status()
# print(response.text)
#
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{MY_USERNAME}/graphs"
GRAPH_ID = "habit-tracker"
graph_params = {"id":GRAPH_ID,
                "name":"My Habit Tracker",
                "unit":"commit",
                "type":"int",
                "color":"sora",
                }
headers = {
    "X-USER-TOKEN":TOKEN,
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)
quantity = input("How many Pomodoros did you do today?")
now = datetime.now()
today_time_stamp = now.strftime("%Y%m%d")
POST_PIXEL_ENDPONT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
pixel_params= {"date":today_time_stamp,
              "quantity":quantity}
response = requests.post(url=POST_PIXEL_ENDPONT, json=pixel_params, headers=headers)
print(response.text)

# # UPDATE PIXEL
# UPDATE_PIXEL_ENDPOINT = f"{POST_PIXEL_ENDPONT}/{today_time_stamp}"
# update_pixel_params = {
#     "quantity": quantity,
# }
# # response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_pixel_params, headers=headers)
# # print(response.text)
# # DELETE PIXEL
# delete_time_stamp = "20200915"
# DELETE_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{delete_time_stamp}"
#
# response = requests.delete(url=DELETE_PIXEL_ENDPOINT,headers=headers)
# print(response.text)
