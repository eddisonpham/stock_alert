import requests
from twilio.rest import Client
import json
import random
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = " RZ71JJGZ1RNZ75YU"

account_sid = "AC66fe244187dc027510063aeada19e93d"
auth_token = "6c13d62650d5ace6833b93df9caf51e9"

NEWS_API = "581d6ec07ee3478f86fac7b4b5c2b59b"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_param={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":API_KEY
}


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
response = requests.get(url, params=stock_param)
data = response.json()["Time Series (Daily)"]
n = json.dumps(data, indent=2)
data_list = [value for (key, value) in data.items()]
yesterday = float(data_list[0]['4. close'])
day_before_yesterday = float(data_list[1]['4. close'])
difference = yesterday-day_before_yesterday
if yesterday >= day_before_yesterday:
    diff_percent = (difference / yesterday) * 100
else:
    diff_percent = (difference / day_before_yesterday) * 100

news_params = {
    "apiKey": NEWS_API,
    "qInTitle": COMPANY_NAME
}
news_response = requests.get(NEWS_ENDPOINT, params=news_params)
articles = news_response.json()["articles"]
three_articles = articles[:3]
if diff_percent<0:
    text = f"{STOCK} 🔻{abs(diff_percent)}%\n"
elif diff_percent>0:
    text = f"{STOCK} 🔺 {abs(diff_percent)}%\n"
if diff_percent!=0:
    news = [f"{text}Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    for article in news:
        # client = Client(account_sid, auth_token)
        # message = client.messages.create(
        #     body=f"{article}",
        #     from_="+15305075675",
        #     to="4165205379"
        # )
        print(article)



