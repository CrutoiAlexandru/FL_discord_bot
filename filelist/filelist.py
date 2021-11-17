# import requests
# from requests.auth import HTTPBasicAuth
import feedparser
import config

def get_rss_feed():
    feed = feedparser.parse("https://filelist.io/rss.php?username=" + config.USERNAME + "&passkey=" + config.PASSKEY)

    print(feed.entries[0].title)
    return feed.entries[0].title

def run():
    return get_rss_feed()