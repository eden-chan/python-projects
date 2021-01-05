import os
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from date_check import is_date
import pandas as pd

link = "https://www.amazon.ca/All-new-Kindle-Paperwhite-Waterproof-Storage/dp/B07HKYZMQX/ref=sr_1_1?dchild=1&keywords=kindle&qid=1609780388&sr=8-1"
wish_list_links = []

dp_index = link.index('/dp/') + 4
ref_index = link.index('/ref')
product_code = link[dp_index:ref_index]


camel_link = f"https://ca.camelcamelcamel.com/product/{product_code}?context=search"
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4307.0 Safari/537.36 Edg/88.0.692.0"
accept_lang = "en-GB,en;q=0.9,en-US;q=0.8"
headers = {"User-Agent": user_agent, "Accept-Language": accept_lang}

wish_list_url = 'https://www.amazon.ca/hz/wishlist/ls/ref=wl_tabs_your_lists?isYourLists=true'
wl_response = requests.get(url=wish_list_url, headers=headers)

wl_soup = BeautifulSoup(wl_response.text, 'html.parser')
# print(wl_soup.prettify())
wl_links = wl_soup.select(selector="#item-page-wrapper.a-section")
print(wl_links)

response = requests.get(url=link, headers = headers)
soup = BeautifulSoup(response.text, 'html.parser')

camel_response = requests.get(url=camel_link, headers= headers)
camel_soup = BeautifulSoup(camel_response.text, 'html.parser')

price_table_td = camel_soup.select(selector="table.product_pane tr td")

table_prices = [td.getText() for td in price_table_td if not td.getText().find('$')==-1]
average_price = float(table_prices[3][1:])
lowest_price = float(table_prices[2][1:])
lowest_price_date = [td.getText() for td in price_table_td if is_date(td.getText())][2]
print(lowest_price_date)
print(lowest_price)
print(average_price)

item_name = soup.select_one(selector='#productTitle').getText().strip()
current_price = float(soup.select_one(selector="#priceblock_ourprice").getText().split()[1])
print(current_price)

from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

TWILIO_AUTH_TOKEN = "bf72c5f05c07f8ed53d90d02ebf2be61"
TWILIO_ACCOUNT_SID = "AC6380bdd9461307da170e0f401b21c480"
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)#, http_client=proxy_client)

message_text = f"""{item_name} is now at ${current_price} with an 
        average price of ${average_price}, and lowest price of ${lowest_price} last seen in {lowest_price_date}"""
# message = client.messages.create(
#                      body=message_text,
#                      from_='+19382385586',
#                      to='+1 647-766-2052'
#                  )
#
# print(message.status)

