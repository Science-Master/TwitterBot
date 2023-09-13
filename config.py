import tweepy
import time

#AUTHENTICATE TO TWITTER
consumer_key = "t1mZcV9xIxsNIWzRLCNunVLic"
consumer_secret = "rLosXdn6TEUm9JUfkK38HPlHjwce4mkONmeHe1Jyl2uzgTaAQi"
access_token = "1276672262993776642-5bOWawuVXPvgtvtw6M7CF55IjWUSL2"
access_token_secret = "ieCAhPrRFrwhhnSQUCMqcS9sO1LphSX6PpKV3s9CJNiEb"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

FILE_NAME = "last_seen.txt"
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, "r")
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, "w")
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = "extended")
    for tweet in reversed(tweets):
        if "#entanglement" in tweet.full_text.lower():
            print(str(tweet.id) + "-" + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + "wow wow woi :", tweet.id)
            api.create_favorite(tweet.id)
            #api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)
            print(tweet.text)

while True:
    reply()
    time.sleep(2)

