import feedparser
import config

def run():
    # aquires the rss feed from filelist, needs login
    feed = feedparser.parse("https://filelist.io/rss.php?username=" + config.USERNAME + "&passkey=" + config.PASSKEY)
    #return feed's latest torrent title
    return feed.entries[0].title
