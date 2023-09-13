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

for tweet in tweepy.Cursor(api.search, q=('#Polio OR #SPFx -filter:retweets'), lang='en').items(5):
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, q=('#Arduino OR #GIS OR #Python OR #EndPolio OR #Triathlon-filter:retweets'),lang='en').items(10):
            try:
                # Add \n escape character to print() to organize tweets
                print('\nTweet by: @' + tweet.user.screen_name)

                # Retweet tweets as they are found
                tweet.favorite()
                print('Like the tweet')

                time.sleep(3)

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break