from time import gmtime
import pytz
from bs4 import BeautifulSoup
from dateutil import parser
import utils
import config
import regex


def format_item(item, feedinfo, channelid):
    category = config.get_feed_category(channelid, feedinfo)
    format = config.get_format_by_category(channelid, category)

    title = utils.get_entry(item, 'title')
    pubdate = format_date(utils.get_entry(item, 'published'))
    author = utils.get_entry(item, 'author')
    link = utils.get_entry(item, 'link')
    author = utils.get_entry(item, 'author')
    hashtags = '#'.join(feedinfo['tags'])

    desc = format_description(utils.get_entry(item, 'description'))
    desc = BeautifulSoup(desc).get_text()

    posttext = utils.format_str(format, author=author, title=title,
                                body=desc, url=link, hashtags=hashtags, pubdate=pubdate)
    return posttext

def format_date(date: str):
    parsed = parser.parse(date)
    gmt = str(pytz.timezone('GMT').normalize(parsed))
    return gmt.replace('+00:00', ' GMT')

def format_description(description):
    return
