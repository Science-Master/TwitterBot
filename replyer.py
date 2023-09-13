import tweepy
import time
import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#AUTHENTICATE TO TWITTER
consumer_key = "t1mZcV9xIxsNIWzRLCNunVLic"
consumer_secret = "rLosXdn6TEUm9JUfkK38HPlHjwce4mkONmeHe1Jyl2uzgTaAQi"
access_token = "1276672262993776642-5bOWawuVXPvgtvtw6M7CF55IjWUSL2"
access_token_secret = "ieCAhPrRFrwhhnSQUCMqcS9sO1LphSX6PpKV3s9CJNiEb"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit_notify=True)


def weeklyTweet ():
    if datetime.date.today().weekday() == 0:
        dailyTweet = "Hello everyone, today is Monday"
    if datetime.date.today().weekday() == 1:
        dailyTweet = "hello everyone, today is Tuesday"
    if datetime.date.today().weekday() == 2:
        dailyTweet = "Hello everyone, today is Wednesday"
    if datetime.date.today().weekday() == 3:
        dailyTweet = "Hello everyone, today is Thursday"
    if datetime.date.today().weekday() == 4:
        dailyTweet = "Hello everyone, today is Friday"
    if datetime.date.today().weekday() == 5:
        dailyTweet = "Hello everyone, today is Saturday"
    if datetime.date.today().weekday() == 6:
        dailyTweet = "Hello everyone, today is Sunday"

   # api.update_status(dailyTweet)
    print(dailyTweet)

weeklyTweet()
time.sleep(8400)

