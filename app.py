# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

import os
import sys
import time

from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    ButtonsTemplate, URITemplateAction, PostbackTemplateAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent, ImagemapSendMessage, BaseSize, URIImagemapAction, MessageImagemapAction, ImagemapArea
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
#channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
#channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
channel_secret = '4fa72238672c25a970d378eb364ac3af'
channel_access_token = 'hb8oE3kH7ys+kpqrUcKCEeAii6gvsAmf4hKTJzffNe6VEkcptKpdczTKs7BHuxlkN3JbH8731E1D7/h/4Lu2L5gjKrTTW9kpwGTcZd7w+tpw/RPQEWWILrhfePT0s2nUe2M+O50e1NOPVUpNAF3emwdB04t89/1O/w1cDnyilFU='


if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if event.beacon.type == 'enter':
            time.sleep(3)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="สวัสดี\nhttp://amzn.asia/cmpStQk")
            )
            """
            line_bot_api.reply_message(
                event.reply_token,
                ImagemapSendMessage(
                    base_url='https://www.dropbox.com/s/g2x56fis4wtfzin/31Yi8xKclrL.jpg?dl=0',
                    alt_text='あなたのトイレです。',
                    base_size=BaseSize(height=1040, width=1040),
                    actions=[
                        URIImagemapAction(
                            link_uri='http://amzn.asia/cmpStQk',
                            area=ImagemapArea(
                                x=0, y=0, width=520, height=1040
                            )
                        ),
                        MessageImagemapAction(
                            text='hello',
                            area=ImagemapArea(
                                x=520, y=0, width=520, height=1040
                            )
                        )
                    ]
                )
            )
            """
        
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        
        '''
        if event.type == 'message':
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Beacon")
            )
        '''
        
        '''
        @handler.add(BeaconEvent)
        def handle_beacon(event):
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Got beacon event. hwid=' + event.beacon.hwid))
        '''
        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="HEY")
        )

    return 'OK'


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port 80] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()
    print 'OK'
    app.run(debug=options.debug, port=options.port)
