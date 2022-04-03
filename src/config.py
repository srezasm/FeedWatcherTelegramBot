import ConfigSingleton

def get_bot_token():
    return ConfigSingleton.config_dic['bot-token']

def get_watch_delay():
    return ConfigSingleton.config_dic['watch-delay']

def get_log_mail_address():
    return ConfigSingleton.config_dic['log-mail-address']

def get_log_mail_pass():
    return ConfigSingleton.config_dic['log-mail-pass']

def get_channels():
    return list(ConfigSingleton.config_dic['channels'])

def get_channel_feeds(channelid):
    return list(ConfigSingleton.config_dic['channels'][channelid]['feeds'])

def get_feed_info(channelid, feedname):
    return ConfigSingleton.config_dic['channels'][channelid]['feeds'][feedname]

def get_feed_category(channelid, feedname):
    return ConfigSingleton.config_dic['channels'][channelid]['feeds'][feedname]['category']

def get_format_by_category(channelid, category):
    return ConfigSingleton.config_dic['channels'][channelid]['formats'][category]

def get_ids():
    return ConfigSingleton.config_dic['idsfile']

def get_etags():
    return ConfigSingleton.config_dic['etagsfile']

def write_ids(newids: str):
    with open(get_ids(), 'w') as fw:
        fw.write(newids)

def write_etags(newetag: str):
    with open(get_etags(), 'w') as fw:
        fw.write(newetag)
