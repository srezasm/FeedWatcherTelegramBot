import config
import feedhandler
import json
import ConfigSingleton
import formathandler

# ------- Initiate the Singleton values -------
config_file = open('./config.json')
config_dic = json.load(config_file)['bot-token']
ConfigSingleton.config_dic = config_dic


for chl in config.getchannels():
	newitems = []
	for feed in config.getchannelfeeds(chl):
		feedinfo = config.getfeedinfo(feed)

		items = feedhandler.fetch_new_items(feedinfo)
		for item in items:
			newitems.append(formathandler.format_item(item, feedinfo, chl))
		
