import config
import feedhandler

for chl in config.getchannels():
	for feed in config.getchannelfeeds(chl):
		newitems = feedhandler.fetchnewitems(config.getfeedinfo(feed))