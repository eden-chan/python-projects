import requests
from datetime import datetime, timedelta
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHAVANTAGE_API_KEY = "OW6Z2FUX24Y719MO"
NEWS_API_KEY = "4ec97593a6b64319827860f6b1667d86"
NUMBER_OF_TOP_ARTICLES = 5
MIN_ELASTICITY = 2
TWILIO_AUTH_TOKEN = "bf72c5f05c07f8ed53d90d02ebf2be61"
TWILIO_ACCOUNT_SID = "AC6380bdd9461307da170e0f401b21c480"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": ALPHAVANTAGE_API_KEY
}
response = requests.get(url=STOCK_ENDPOINT,params=parameters)
response.raise_for_status()

now = datetime.now()
today_date = now.strftime('%Y-%m-%d')
yesterday_date = (now - timedelta(1)).strftime('%Y-%m-%d')
day_before_yesterday_date = (now - timedelta(2)).strftime('%Y-%m-%d')


print(today_date)
print(yesterday_date)

daily_stock_data = response.json()["Time Series (Daily)"]
past_week_closing_prices = {key:value["4. close"] for (key,value) in daily_stock_data.items()}
past_trading_days = list(daily_stock_data.keys())
previous_trading_date = past_trading_days[1]
second_previous_trading_date = past_trading_days[2]

yesterday_closing_price = float(past_week_closing_prices[previous_trading_date])
day_before_yesterday_closing_price = float(past_week_closing_prices[second_previous_trading_date])

percentage_difference = (yesterday_closing_price - day_before_yesterday_closing_price) / ((yesterday_closing_price - day_before_yesterday_closing_price)/2)
positive_percentage_difference = abs(percentage_difference)
if positive_percentage_difference >= MIN_ELASTICITY:
    if percentage_difference >= MIN_ELASTICITY:
        stock_percentage_change_message = f"{STOCK_NAME}🔺{positive_percentage_difference}%"
    elif percentage_difference <= -1 * MIN_ELASTICITY:
        stock_percentage_change_message = f"{STOCK_NAME}🔻{positive_percentage_difference}%"


    news_parameters = {
       "q": COMPANY_NAME,
       "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    top_articles = news_response.json()["articles"][:NUMBER_OF_TOP_ARTICLES]
    top_article_headlines = {article["title"]:{"description": article["description"], "link": article["url"]} for article in top_articles}

    for headline in top_article_headlines.keys():
        description = top_article_headlines[headline]["description"]
        link = top_article_headlines[headline]["link"]
        # proxy_client = TwilioHttpClient()
        # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)#, http_client=proxy_client)


        message = client.messages.create(
                             body=f"{stock_percentage_change_message}\nHeadline: {headline}\n Description: {description}\n{link}",
                             from_='+19382385586',
                             to='+1 647-766-2052'
                         )
        print(message.status)







    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻🔺5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

