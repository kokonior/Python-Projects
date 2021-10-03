import feedparser, time

subreddits = ["reddit.com/r/python/new.rss"]#subreddits so display titles from
while True:
    for sub in subreddits:
        feed = feedparser.parse(sub)
        for entry in feed.entries:
            print(entry['title'])#print post title
            time.wait(60)#wait 60 seconds to fetch new posts