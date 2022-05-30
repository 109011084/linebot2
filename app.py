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

line_bot_api = LineBotApi('T0LrU5OiSDzKrYxNa6+7gMhRSm1fhlgv/rKlMUvB4+/kKV7y1SlmA/cfWBRQCi/QIKnsvaGwFwBZQEV4OOZi6uZZfD1eL9L7O9gZUhH3n0obecaur/BT9AL4k1rf/ovWiaRGDI0v1KBW80nyD80RvwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('118a21f5bdead17ad3b92b9db18f0281')


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
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='早安！'))


if __name__ == "__main__":
    app.run()