import twitter


def twitter_conn():
    CONSUMER_KEY = 'xxxxxx'
    CONSUMER_SECRET = 'xxxxxxx'
    OAUTH_TOKEN = '-xxxxxxx'
    OAUTH_TOKEN_SECRET = 'xxxxxx'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api


