import config
import feedhandler
import json
import Singleton

# ------- Initiate the Singleton values -------
config_file = open('./config.json')
config_dic = json.load(config_file)['bot-token']
Singleton.config_dic = config_dic


for chl in config.getchannels():
	for feed in config.getchannelfeeds(chl):
		newitems = feedhandler.fetchnewitems(config.getfeedinfo(feed))
