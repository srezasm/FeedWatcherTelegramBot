from telegram.ext import ExtBot as bot
import config
import requests

token = config.get_bot_token()


def send_message(text: str, channelname: str, disablenotification=False, disablelinkpreview=True):
    text = text.replace('.', '\\.')
    text = text.replace('!', '\\!')

    requrl = 'https://api.telegram.org/bot%s/sendMessage?chat_id=@%s&disable_web_page_preview=%s&disable_notification=%s&text=%s&parse_mode=html' % (token, channelname, disablelinkpreview, disablenotification, text)
    req = requests.post(requrl)
    print(requrl)
    print(req.json())

# TODO: upload youtube videos
# def send_video(video: str, channelname: str, caption='', disablenotification=False, disablelinkpreview=True):
#     requrl = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=@{channelname}&disable_web_page_preview={disablelinkpreview}&disable_notification={disablenotification}&parse_mode=MarkdownV2&supports_streaming=True&caption={caption}'
#     vid = files = {'document': open(video, 'rb')}
