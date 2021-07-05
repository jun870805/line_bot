Line 聊天機器人 架設 
==================
![](https://github.com/jun870805/line_bot/blob/1.0.1/Image/Image.jpg?raw=true)

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
    *   [登入Heroku帳號](#Step3-1)
    *   [建立](#em)
    *   [程式碼](#code)
    *   [圖片](#img)
*   [Line Bot 最終設定](#misc)
    *   [設定Webhook](#backslash)
    *   [](#autolink)
*   [成果展示](#misc)
    *   [跳脫字元](#backslash)
    *   [自動連結](#autolink)


<h2 id="Step1">創建Line Bot</h2>

<h3 id="Step1-1">登入Line帳號</h3>

![](https://github.com/jun870805/line_bot/blob/1.0.1/Image/LoginLine.png?raw=true)

<h3 id="Step1-2">建立服務提供者</h3>

![](https://github.com/jun870805/line_bot/blob/1.0.1/Image/NewProvider.png?raw=true)

<h3 id="Step1-3">建立頻道</h3>

選擇Create a Messaging API channel
![](https://github.com/jun870805/line_bot/blob/1.0.1/Image/chooseType.png?raw=true)

channel icon (選填) ： 上傳聊天機器人logo圖片

channel name (必填) ： 設定聊天機器人名稱

channel description (必填) ： 設定聊天機器人描述

![](https://github.com/jun870805/line_bot/blob/1.0.1/Image/CreateChannel1.png?raw=true)
Category (必填) ： 選擇聊天機器人類別

Subcategory (必填) ： 選擇聊天機器人類別細項

Email address (必填) ： 設定信箱

Privacy policy URL (選填) ： 不用填

Team of use URL (選填) ： 不用填

最下面記得打勾！！

![](https://github.com/jun870805/line_bot/blob/1.0.1/Image/CreateChannel2.png?raw=true)

<h3 id="Step1-4">取得頻道參數</h3>

在Basic settings頁面複製channel_secret
![](https://github.com/jun870805/line_bot/blob/1.0.1/Image/channel_secret.png?raw=true)
在Messaging API settings頁面複製Channel access token
![](https://github.com/jun870805/line_bot/blob/1.0.1/Image/channel_access_token.png?raw=true)


**NOTE:** Line Bot Messaging API 詳細設定說明請[按此][line-eng-doc].

[line-eng-doc]:https://developers.line.biz/en/docs/messaging-api/


<h2 id="Step2">Flask Web Server</h2>

<h3 id="Step2-1">資料夾內檔案</h3>

![](https://github.com/jun870805/line_bot/blob/1.0.1/Image/FilePackage.png?raw=true)

<h3 id="Step2-2">requirements.txt</h3>

    gunicorn  # Python WSGI
    flask
    flask_socketio
    flask_cors
    line-bot-sdk   # line bot 使用 
    requests  # 爬蟲PTT網站使用
    beautifulsoup4  # 爬蟲PTT網站使用

<h3 id="Step2-3">config.ini</h3>

<h3 id="Step2-4">app.py</h3>

<h3 id="Step2-5">Procfile</h3>


<h2 id="Step3">Heroku 部署</h2>

<h3 id="Step3-1">登入Heroku帳號</h3>

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

