from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import random

app = Flask(__name__)

line_bot_api = LineBotApi('27xL1uDr5z7jHkjiXYXQmDbCW4pj6xYEKLEpa8DW72xmOBa5htCEVUgCBFpjvj5VDuljhLqVizFiv24swJcAmcGvTixVff++g8dZBvAylXflp2taMBxr96+jTqeKI5lGQ7Ln0AXdZqYKwviZ81SUtgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('930e19c7c9908f837fb23189879d331e')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    r = random.randint(1, 2)
    msg = event.message.text
    if msg == '今天要吃什麼':
        s = '等我一下'
        if r == 1:
            s = '今天吃豬'
        elif r == 2:
            s = '今天吃魚'
    elif meg == '謝謝你':
        s = '不客氣'
    else:
        s = '滾' 
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()