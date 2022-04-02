import json

def getbottoken():
    with open('config.json') as fr:
        return json.load(fr)['bot-token']

def getwatchdelay():
    with open('config.json') as fr:
        return json.load(fr)['watch-delay']

def getlogmailaddress():
    with open('config.json') as fr:
        return json.load(fr)['log-mail-address']

def getlogmailpass():
    with open('config.json') as fr:
        return json.load(fr)['log-mail-pass']

def getchannels():
    with open('config.json') as fr:
        return list(json.load(fr)['channels'])

def getchannelfeeds(channelid):
    with open('config.json') as fr:
        return list(json.load(fr)['channels'][channelid]['feeds'])

def getfeedinfo(channelid, feedname):
    with open('config.json') as fr:
        return json.load(fr)['channels'][channelid]['feeds'][feedname]

def getfeedcategory(channelid, feedname):
    with open('config.json') as fr:
        return json.load(fr)['channels'][channelid]['feeds'][feedname]['category']

def getformatbycategory(channelid, category):
    with open('config.json') as fr:
        return json.load(fr)['channels'][channelid]['formats'][category]

def getids():
    with open('config.json') as fr:
        return json.load(fr)['idsfile']

def getetags():
    with open('config.json') as fr:
        return json.load(fr)['etagsfile']

def writeids(newids: str):
    with open(getids(), 'w') as fw:
            fw.write(newids)

def writeetags(newetag: str):
    with open(getids(), 'w') as fw:
            fw.write(newetag)
