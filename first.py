from tweepy import Stream
from tweepy.streaming import StreamListener
import tweepy
from tweepy import OAuthHandler
import json

consumer_key = '-'
consumer_secret = '-'
access_token = '-'
access_secret = '-'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


def process_or_store(tweet):
    print(json.dumps(tweet))


# code to read our twitter timeline
for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)

# no idea what this does?? Save for later :/ ?
# for status in tweepy.Cursor(api.home_timeline).items(10):
#     print(status._json)

#prints the list of followers

# for friend in tweepy.Cursor(api.friends).items():
#     process_or_store(friend.screen_name)


# for tweet in tweepy.Cursor(api.user_timeline).items():
    # process_or_store(tweet.text)

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])
