Line 聊天機器人 架設 
==================
<img src="https://github.com/jun870805/line_bot/blob/1.0.1/Image/Architecture.png" width="375">

目錄
================

*   [創建Line Bot](#Step1)
    *   [登入Line帳號](#Step1-1)
    *   [建立服務提供者](#Step1-2)
    *   [建立頻道](#Step1-3)
    *   [取得頻道參數](#Step1-4)
*   [Flask Web Server](#Step2)
    *   [資料夾內檔案](#Step2-1)
        *   [requirements.txt](#Step2-2)
        *   [config.ini](#Step2-3)
        *   [app.py](#Step2-4)
        *   [Procfile](#Step2-5)
*   [Heroku 部署](#Step3)
*   [Line Bot 最終設定](#Step4)
*   [成果展示](#Step5)


<h2 id="Step1">創建Line Bot</h2>

<h3 id="Step1-1">登入Line帳號</h3>

<img src="hhttps://github.com/jun870805/line_bot/blob/1.0.1/Image/LoginLine.png" width="375">

<h3 id="Step1-2">建立服務提供者</h3>

<img src="https://github.com/jun870805/line_bot/blob/1.0.1/Image/NewProvider.png" width="375">

<h3 id="Step1-3">建立頻道</h3>

選擇Create a Messaging API channel
<img src="https://github.com/jun870805/line_bot/blob/1.0.1/Image/chooseType.png" width="375">

channel icon (選填) ： 上傳聊天機器人logo圖片

channel name (必填) ： 設定聊天機器人名稱

channel description (必填) ： 設定聊天機器人描述

<img src="https://github.com/jun870805/line_bot/blob/1.0.1/Image/CreateChannel1.png" width="375">

Category (必填) ： 選擇聊天機器人類別

Subcategory (必填) ： 選擇聊天機器人類別細項

Email address (必填) ： 設定信箱

Privacy policy URL (選填) 

Team of use URL (選填) 

最下面記得打勾！！

<img src="https://github.com/jun870805/line_bot/blob/1.0.1/Image/CreateChannel2.png" width="375">

<h3 id="Step1-4">取得頻道參數</h3>

在Basic settings頁面複製channel_secret

<img src="https://github.com/jun870805/line_bot/blob/1.0.1/Image/channel_secret.png" width="375">

在Messaging API settings頁面複製Channel access token

<img src="https://github.com/jun870805/line_bot/blob/1.0.1/Image/channel_access_token.png" width="375">

**NOTE:** Line Bot Messaging API 詳細設定說明請[按此][line-eng-doc].

[line-eng-doc]:https://developers.line.biz/en/docs/messaging-api/


<h2 id="Step2">Flask Web Server</h2>

<h3 id="Step2-1">資料夾內檔案</h3>

<img src="https://github.com/jun870805/line_bot/blob/1.0.1/Image/FilePackage.png" width="375">

<h3 id="Step2-2">requirements.txt</h3>
<h3>Heroku會安裝這裡面的python套件</h3>

    gunicorn  # Python WSGI
    flask
    flask_socketio
    flask_cors
    line-bot-sdk   # line bot 使用 
    requests  # 爬蟲PTT網站使用
    beautifulsoup4  # 爬蟲PTT網站使用

<h3 id="Step2-3">config.ini</h3>
<h3>app裡使用到的設定檔(將剛剛複製下來的參數加到檔案)</h3>

    [line-bot]
    channel_access_token = [your_channel_access_token]
    channel_secret = [your_channel_secret]

<h3 id="Step2-4">app.py</h3>
<h3>主要執行Flask程式</h3>

宣告Flask app

    app = Flask(__name__) 

LINE 聊天機器人的基本資料設定

    config = configparser.ConfigParser()
    config.read('config.ini')

    line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
    handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

接收LINE資訊

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

回應使用者輸入的文字

    @handler.add(MessageEvent, message=TextMessage)
    def response(event):
        
        # Line bot Verify驗證 帳號排除 
        if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
            
            response_text = ""
            for i in event.message.text:
                response_text += i
        
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=response_text)
            )

增加抓取PTT Stock 文章列表

    Name = event.message.text.split("-")[1]
    url = "https://www.ptt.cc/bbs/Stock/search?q=author:"+Name            r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.select("div.title")
    for item in results:
        a_item = item.select_one("a")
        title = item.text
        response_text += title+"\n"

Flask 啟動

    app.run()


<h3 id="Step2-5">Procfile</h3>
<h3>Heroku執行語法</h3>

    web: gunicorn app:app [檔案名稱:Flask宣告參數]


<h2 id="Step3">Heroku 部署</h2>

登入帳號：

    heroku login

初始化目錄

    git init

創建新的heroku專案

    heroku create [yourname]

設定專案簡稱heroku

    heroku git:remote -a [yourname]

將資料夾內檔案更動提交到staging area(索引)

    git add .

提交版本並加上訊息

    git commit -a -m "update heroku"

推送到遠端

    git push heroku HEAD:master

看heroku logs

    heroku logs --tail

最後成功網址：

    https://[yourname].herokuapp.com/callback



<h2 id="Step4">Line Bot 最終設定</h2>

將網址輸入在Messaging API settings頁面並開啟Use webhook

<img src="https://github.com/jun870805/line_bot/blob/1.0.1/Image/SettingWebhook.png" width="375">

**NOTE:** Webhook 的原理 (截自[開發LINE聊天機器人不可不知的十件事][Webhook-doc].)

[Webhook-doc]:https://engineering.linecorp.com/zh-hant/blog/line-device-10/)

<img src="https://github.com/jun870805/line_bot/blob/1.0.1/Image/Webhook.png" width="375">

<h2 id="Step5">成果展示</h2>

可以透過Messaging API settings頁面的QR code 加入好友並使用～～

<img src="https://github.com/jun870805/line_bot/blob/1.0.1/Image/result.png" width="375">