import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
me = api.me()
# print(me.followers_count)

# HELPER FUNCTION TO HANDLE THE RATE LIMIT ERROR
def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1)
    except StopIteration:
        print('end of iteration')



# GENEROUS BOT THAT FOLLOWS ALL THAT FOLLOW ME
# for follower in  limit_handle(tweepy.Cursor(api.followers).items()):
#     print(follower.name)
#     print(follower.followers_count)
#     if follower.name == 'Stephanie Corsi':
#         follower.follow()


# BOT TO SEARCH TWEETS, RETWEET AND LIKE THEM
searchString = 'Andrei Neagoie'
numbersOfTweets = 2
for tweet in limit_handle(tweepy.Cursor(api.search, searchString).items(numbersOfTweets)):
    try:
        # tweet.favorite()
        # tweet.retweet()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)


exit()