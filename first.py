import tweepy
from tweepy import OAuthHandler

consumer_key = '7zr5UjT1dcroqKI1IckxgEVOw'
consumer_secret = 'PhIbzQ1VmecS3OP7ZiukoiHq8BBVOqKWYYLHdrhjatOvpVXvgr'
access_token = '2995486416-wrstd3gE7i83vvr3bLjNd7Y6BXkDrUEw2DhWvwD'
access_secret = 'HlOuor0ujivGsFP4SuHrVeasOQp4kfK2SWTkJWs8PTAzv'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
