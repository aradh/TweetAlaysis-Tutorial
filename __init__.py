import TweetsAnalysis.twitterapi as twitterapi
import TweetsAnalysis.anatomytwitter as anatomytwitter
import json



if __name__ == '__main__':
    try:
        # connection to twitter api
        conn = twitterapi.twitter_conn()
    except:
        exit()

    var = input("Please enter something: ")
    print("You entered " + str(var))

    count = 100
    from urllib.parse import unquote

    search_results = conn.search.tweets(q=var, count=count)
    statuses = search_results['statuses']
    for _ in range(5):
        print('Length of statuses', len(statuses))
        try:
            # '?max_id=984894360788479999&q=%23HDFC&count=100&include_entities=1'
            next_results = search_results['search_metadata']['next_results']
        except KeyError as e:
            print("exception occured")

    kwargs = dict([kv.split('=') for kv in unquote(next_results[1:]).split('&')])
    search_results = conn.search.tweets(**kwargs)
    statuses += search_results['statuses']

    status_texts = [status['text'] for status in statuses]

    screen_names = [user_mention['screen_name']
                    for status in statuses
                    for user_mention in status['entities']['user_mentions']]
    hashtags = [hashtag['text']
                for status in statuses
                for hashtag in status['entities']['hashtags']]
    # compute a collection of all words from all tweets

    words = [w
             for t in status_texts
             for w in t.split()]

    # explore the first 5 time for each

    print(json.dumps(status_texts[0:5], indent=1))
    print(json.dumps(screen_names[0:5], indent=1))
    print(json.dumps(hashtags[0:5], indent=1))
    print(json.dumps(words[0:5], indent=1))

    from collections import Counter

    for item in [words, screen_names, hashtags]:
        c = Counter(item)
        print(c.most_common()[:10])  # top 10
        print()

    # Using prettytable to display tuples in a nice tabular format

    from prettytable import PrettyTable

    for label, data in (('Word', words), ('Screen_Name', screen_names),
                        ('hashtag', hashtags)):
        pt = PrettyTable(field_names=[label, 'count'])
        c = Counter(data)
        [pt.add_row(kv) for kv in c.most_common()[:10]]
        pt.align[label], pt.align['count'] = 'l', 'r'  # set column alignment
        print(pt)


    # calculating lexical diversity for tweets-
    # ..............Calculating lexical diversity for tweets....................

    def lexical_diversity(tokens):
        return len(set(tokens)) / len(tokens)


    # .......a function for computing the averge number of words for tweet..................

    def average_words(statuses):
        total_words = sum([len(s.split()) for s in statuses])
        return total_words / len(statuses)


    print(lexical_diversity(words))
    print(lexical_diversity(screen_names))
    print(lexical_diversity(hashtags))
    print(lexical_diversity(status_texts))

    # finding the most popular retweets

    # .............store out a tuple of these three values...

    retweets = [
        (status['retweet_count'], status['retweeted_status']['user']['screen_name'], status['retweeted_status']['id'],
         status['text'])
        # for each status
        for status in statuses
        # so long as the status meets their condition
        if 'retweeted_status' in status.keys()
        ]

    # slice off the first 5 from the sorted results & display each item in the tuple

    pt = PrettyTable(field_names=['count', 'Screen_Name', 'Tweet ID', 'Text'])
    [pt.add_row(row) for row in sorted(retweets, reverse=True)[:5]]

    pt.max_width['Text'] = 50
    pt.align = 'l'
    print(pt)

    # looking up users who have retweeted a status

    # retweets = twitter_api.statuses.retweets(id = )
    #    print([r['user']['screen_name'] for r in retweets])

    # plotting frequencies of words
    # matplotlib.use('agg')

    from matplotlib import pyplot as plt

    # %umatplotlib inline

    word_counts = sorted(Counter(words).values(), reverse=True)
    plt.loglog("word_counts")
    plt.ylabel("freq")
    plt.xlabel("Word Rank")
    plt.show()

    # generating histograms of words, screen names and hashtags

    for label, data in (('words', words), ('Screen Names', screen_names), ('Hashtags', hashtags)):
        # build a frequency map for each set of data
        # and plot the values
        c = Counter(data)
        plt.hist(list(c.values()))
        # add a tittle and ylabel
        plt.title(label)
        plt.ylabel("Number of items in bin")
        plt.xlabel("Bins(number of times an item appeared)")
        # &display as a new fig
        plt.show()

    # generating a histogram of retweet counts
    # ......using underscores while unpacking values in
    # ..........a table is idiomatic for discarding them
    counts = [count for count, _, _, _ in retweets]

    plt.hist(counts)
    plt.title('retweets')
    plt.xlabel('Bin(number of times retweets)')
    plt.ylabel('Number of tweets in bin')
    plt.show()




