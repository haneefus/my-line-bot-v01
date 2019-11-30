from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)

line_bot_api = LineBotApi('4d3VCVEliW7/n6oUwfZ4joD9LeQx1QfYpn/2npkunlF39H/inwXxWDQdPnx4RKyDr41ivUnkoy+CXlSuvw2qwu9o1y3+CK7U/iteETlP3pHLvfSlLq5QHBVwxiUcvfn4gdzMkAjbA1NJuL3CkxMqDgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('08a777f82eb2e54cbdaf76b784e1cd18')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
