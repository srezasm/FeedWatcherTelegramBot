import pytz
from dateutil import parser
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
    link = f'[Link]({utils.get_entry(item, "link")})'
    author = utils.get_entry(item, 'author')
    hashtags = '\\%23\\'.join(feedinfo['tags'])
    name = feedinfo['name']

    desc = format_desc(utils.get_entry(item, 'description'))

    posttext = utils.format_str(format, name=name, author=author, title=title,
                                body=desc, url=link, hashtags=hashtags, pubdate=pubdate)
    return posttext


def format_date(date: str):
    parsed = parser.parse(date)
    gmt = str(pytz.timezone('GMT').normalize(parsed))
    return gmt.replace('+00:00', ' GMT')


def format_desc(description: str):
    description = BeautifulSoup(description).prettify()
    soup = BeautifulSoup(description)

    ans = soup.find_all('a')
    for a in ans:
        ancl = a.get('href')
        if(regex.match('twitter.com/*./status/', ancl)):
            description = description.replace(
                a, '[quted tweet link](%s)' % ancl)
        else:
            description = description.replace(a, '[link](%s)' % ancl)
        description.replace(a, '[link](%s)' % ancl)

    brs = soup.find_all('br')
    for br in brs:
        description.replace(br, '\n')

    imgs = soup.find_all('img')
    for img in imgs:
        description.replace(img, '[image](%s)' % img.get('src'))

    vids = soup.find_all('video')
    for vid in vids:
        description.replace(vid, '[video](%s)' % vid.get('src'))

    bs = soup.find_all(['b', 'strong'])
    for b in bs:
        description.replace(b, '*%s*' % b.string)

    itals = soup.find_all(['i', 'em'])
    for i in itals:
        description.replace(i, '_%s_' % i.string)

    heads = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for h in heads:
        description.replace(h, '▍*%s*\n' % h.string)

    return regex.sub(r'([_*[]()~`>+-=|{}.!])', r'\\\1', soup.get_text('\n').replace('#', '\\%23\\'))


# def format_description(description: str):
#     # replace img tags with markdown link
#     for img in regex.findall('<img .*?>', description):
#         imgl = regex.search(
#             '(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])', img).group()
#         description = description.replace(img, f'[image]({imgl})')

#     # replace video tags with markdown link
#     for vid in regex.findall('<video .*?>', description):
#         vidl = regex.search(
#             '(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])', vid).group()
#         description = description.replace(vid, f'[link]({vidl})')

#     # replace anchor tags with markdown link
#     for anc in regex.findall('<a.*?>(.*?)(<\/)?a>', description):
#         ancl = regex.search(
#             '(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])', anc).group()
#         if(regex.match('twitter.com/*./status/', ancl)):
#             description = description.replace(
#                 anc, f'[quted tweet link]({ancl})')
#         else:
#             description = description.replace(anc, f'[link]({ancl})')

#     # replace bold/strong tags with markdown bold
#     for bld in regex.findall('<(strong|b).*?>(.*?)(<\/)?(strong|b)>', description):
#         txt = regex.search(
#             '<(strong|b).*?>(.*?)(<\/)?(strong|b)>', bld).group(2)
#         description = description.replace(bld, f'**{txt}**')

#     # replace italic tags with markdown italic
#     for itl in regex.findall('<i.*?>(.*?)(<\/)?i>', description):
#         txt = regex.search('<i.*?>(.*?)(<\/)?i>', itl).group(2)
#         description = description.replace(itl, f'*{txt}*')

#     # replace br tags with newline
#     description = description.replace('<br.*?\/>', '\n')

#     desc = BeautifulSoup(description).get_text('\n')
#     return desc
