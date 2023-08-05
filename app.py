from flask import Flask,request,abort

from line_bot_api import *
from events.basic import *

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    #get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
    #get request body as text
    body = request.get_data(as_text=True)
    app.logger.info('Request body;' + body)

    #handle webhook body
    try:
        hander.handle(body, signature)
    except InvalidSignatureError:
        print('Invalid signature. Please check your channel access token/channel secret')
        abort(400)

    return 'ok'

@hander.add(MessageEvent, message=TextMessage)
def hander_message(event):

    message_text = str(event.message.text).lower()

    if message_text == '@關於我們':
        about_us_event(event)
    
    elif message_text == '@營業據點':
        location_event(event)
if __name__ == '__main__':
    app.run()
    