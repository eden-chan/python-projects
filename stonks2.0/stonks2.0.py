import requests
import yfinance as yf
from csv import reader
import pandas as pd
from datetime import datetime, timedelta
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

stock_names = pd.read_csv('stocks.csv', delimiter=',').to_dict('list')['Stock Name']




NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "4ec97593a6b64319827860f6b1667d86"
NUMBER_OF_TOP_ARTICLES = 3
MIN_ELASTICITY = 5
TWILIO_AUTH_TOKEN = "bf72c5f05c07f8ed53d90d02ebf2be61"
TWILIO_ACCOUNT_SID = "AC6380bdd9461307da170e0f401b21c480"
VIRTUAL_NUMBER = "+19382385586"
VERIFIED_NUMBER = "+1 647-860-7338"

for stock_name in stock_names:
    stock = yf.Ticker(stock_name)
    company_name = stock.info['shortName']
    closing_prices = list(stock.history(period="5d", interval="1d")[2:4].to_dict()['Close'].values())

    past_day_closing_price = closing_prices[0]
    past_day2_closing_price = closing_prices[1]

    # Checks whether the percentage difference of the closing price from past two market days exceeds a given difference
    percentage_difference = (past_day_closing_price - past_day2_closing_price) / ((past_day_closing_price - past_day2_closing_price)/2)
    positive_percentage_difference = abs(percentage_difference)
    if positive_percentage_difference >= MIN_ELASTICITY:
        if percentage_difference >= MIN_ELASTICITY:
            stock_percentage_change_message = f"{stock_name}🔺{positive_percentage_difference}%"
        elif percentage_difference <= -1 * MIN_ELASTICITY:
            stock_percentage_change_message = f"{stock_name}🔻{positive_percentage_difference}%"
        news_parameters = {
           "q": company_name,
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
                                 from_= VIRTUAL_NUMBER,
                                 to= VERIFIED_NUMBER
                             )
            print(message.status)

