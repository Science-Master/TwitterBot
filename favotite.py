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

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                '''tweet.favorite()'''
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)

def main(keywords):
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])
    time.sleep(15)

if __name__ == '__main__':
    main(["football", "soccer", "Barcalona", "liverpool","chelsea", "Asernal", "FIFA", "laliga", "python", "computer", "technology", "data science", "machine learning", "artificial intelligence", "internet", "code", "programming"])

