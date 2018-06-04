from TweetsAnalysis import statuses
import json

status_texts = [status['text'] for status in statuses]

screen_names = [user_mention ['screen_name']
                 for status in statuses
                   for user_mention in status['entities']['user_mentions']]
hashtags = [hashtag['text']
            for status in statuses
               for hashtag in status ['entities']['hashtags']]
#compute a collection of all words from all tweets

words = [w
         for t in status_texts
         for w in t.split()]

#explore the first 5 time for each

print(json.dumps (status_texts[0:5],indent = 1))
print(json.dumps(screen_names[0:5],indent = 1))
print(json.dumps(hashtags[0:5],indent = 1))
print(json.dumps(words[0:5],indent = 1))