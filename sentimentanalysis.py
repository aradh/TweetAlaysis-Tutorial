from TweetsAnalysis.twitterapi import twitter, auth

import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer

twitter_stream = twitter.TwitterStream(auth=auth)
iterator = twitter_stream.statuses.sample()

tweets = []
for tweet in iterator:
    try:
        if tweet['lang'] =='en':
            tweets.append(tweet)
    except:
        pass
    if len(tweets) == 100:
        break

analyzer = SentimentIntensityAnalyzer()
analyzer.polarity_scores('Hello')
analyzer.polarity_scores('I really enjoy this video series.')
analyzer.polarity_scores('I REALLY enjoy this video series!!!')
analyzer.polarity_scores('I REALLY did not enjoy this video series!!!')

scores = np.zeros(len(tweets))
for i, t in enumerate(tweets):
    #..........extract the text portion..................
    text = t['text']

    #.............Measure the polarity of the tweet...........
    polarity = analyzer.polarity_scores(text)

    #..................store the normalized,weighted composite score...................
    scores[i] = polarity['compound']

most_positive = np.argmax(scores)
most_negative = np.argmin(scores)

print('{0:6.3f}: "{1}"'.format(scores[most_positive],tweets[most_positive]['text']))
print('{0:6.3f}: "{1}"'.format(scores[most_negative],tweets[most_negative]['text']))

