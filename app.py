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

app = Flask(__name__)

line_bot_api = LineBotApi('h7rPJ91uUg1HLjO6ZB113IXQsxk9ie3L3jYf98fLLa2Pv9ArX+6Ud14i1hpcYtm3a9u8QpinNEd0JXBYmHBr1MKgX/sf6bZmhQ04cOB/PU2jfqFSrgdzm0iGhPMqGkCmC9c9tr2G1rVxUhiWjrSp+gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('49b63be9f2c3483e383e9f2dd69152ba')


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
    meg = event.message.text
    r = "很抱歉你在問甚麼"

    if msg == 'hi':
        r ='hi'
    elif msg == '吃飽沒':
        r = '還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()