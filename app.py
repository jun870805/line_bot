import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from bs4 import BeautifulSoup
import requests
import configparser
import random

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# Flask GET/POST home 
@app.route("/", methods=['GET','POST'])
def home():
    text = ""
    if request.method == 'GET':
        text = request.args.get('value')
    if request.method == 'POST':
        text = request.form.get('value')

    return "test"+str(text)+"~~~~~"


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# 處理接收到 Line request 後回應
@handler.add(MessageEvent, message=TextMessage)
def response(event):
    
    # Line bot Verify驗證 帳號排除 
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
        response_text = ""
        # 當 message text 之中有ptt才做爬蟲 否則回傳使用者輸入資訊
        if "ptt" in event.message.text.lower():
            # 簡單抓取PTT Stock 文章列表
            try :
                Name = event.message.text.split("-")[1]
                url = "https://www.ptt.cc/bbs/Stock/search?q=author:"+Name
                r = requests.get(url)
                soup = BeautifulSoup(r.text, "html.parser")
                results = soup.select("div.title")
                for item in results:
                    a_item = item.select_one("a")
                    title = item.text
                    response_text += title+"\n"
            except Exception as e :
                response_text = str(e)
        else:
            for i in event.message.text:
                response_text += i
    
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=response_text)
        )

if __name__ == "__main__":
    app.run()
