import ConfigSingleton

def get_bot_token():
    return ConfigSingleton.config_dic['bot-token']

def get_watch_delay():
    return ConfigSingleton.config_dic['watch-delay-minutes']

def get_log_acc_id():
    return ConfigSingleton.config_dic['log-account-id']

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

def get_media_dir():
    return ConfigSingleton.config_dic['mediadir']

def get_log_dir():
    return ConfigSingleton.config_dic['logdir']

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
