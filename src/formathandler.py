from ast import arg
from os import link
from pydoc import describe
from bs4 import BeautifulSoup
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

# Tue, 21 Dec 2021 10:00:00 -0400
# Thu, 01 Nov 2018 00:00:00 +0000
# Fri, 12 Nov 2021 21:52:35 GMT
# 2021-10-31T00:00:00+00:00
# 2022-03-17T17:27:16+03:30
# 2020-07-27T14:56:50+00:00
def format_date(date: str):
    if regex.match('^{3}, \d\d \w{3} \d{4} \d\d:\d\d:\d\d', date):
        region = regex.search('([A-Z]{3})?(\+\d{4})?(\-\d{4})?$', date).group()
        if regex.match('\w{3}', region):
			# log info the match
            region = "+0000"

        date = date.replace(region, '').rstrip()

    if regex.match('', date):
        return

    #! log [date] and details if not found


def format_description(description):
    return
