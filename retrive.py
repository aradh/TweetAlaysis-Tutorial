from TweetsAnalysis.twitterapi import twitter_api

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

print(world_trends)
print()
print(us_trends)


#for trend in us_trends[0]['trends']:
 #   print(trend['name'])
  #  print("Aradhana")
   # print(trend['tweet_volume'])


#Name of tranding tweets in 2 diff geography

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
us_trends_set = set([trend['name'] for trend in us_trends[0]['trends']])
common_trends = world_trends_set.intersection(us_trends_set)
#print(common_trends)

for trend in common_trends:
    print(trend)
#    print("Aradhana")
 #   print(trend['tweet_volume'])
