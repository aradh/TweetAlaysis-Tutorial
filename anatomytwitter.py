from TweetsAnalysis.twitterapi import twitter_conn as twitter_api

q = '#HDFC'

def parse_tweet(query_str):
    count = 100
    from urllib.parse import unquote
    search_results = twitter_api.search.tweets(q=query_str, count = count)
    statuses = search_results['statuses']
    for _ in range(5):
        print('Length of statuses', len(statuses))
        try:
        #'?max_id=984894360788479999&q=%23HDFC&count=100&include_entities=1'
             next_results = search_results['search_metadata']['next_results']
        except KeyError as e:
            print("exception occured")

    kwargs = dict([kv.split('=') for kv in unquote(next_results[1:]).split('&')])
    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']
    return statuses
#print(json.dumps(statuses[0],indent=1))

#prints retweets and faviorite

# region Description
#for i in range(10):
#    print()
#    print("favorites :",statuses[i]['text'])
# endregion