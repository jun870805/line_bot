Line 聊天機器人 架設 
==================
![](https://github.com/jun870805/line_bot/blob/1.0.1/Image/Image.jpg?raw=true)

目錄
================

*   [創建Line Bot](#overview)
    *   [登入Line帳號](#philosophy)
    *   [建立服務提供者](#philosophy)
    *   [建立頻道](#html)
    *   [取得頻道參數](#html)
*   [Flask Web Server](#block)
    *   [段落和換行](#p)
    *   [標題](#header)
    *   [區塊引言](#blockquote)
    *   [清單](#list)
    *   [程式碼區塊](#precode)
    *   [分隔線](#hr)
*   [Heroku 部署](#Step3)
    *   [登入Heroku帳號](#Step3-1)
    *   [建立](#em)
    *   [程式碼](#code)
    *   [圖片](#img)
*   [Line Bot 最終設定](#misc)
    *   [設定Webhook](#backslash)
    *   [打開](#autolink)
*   [成果展示](#misc)
    *   [跳脫字元](#backslash)
    *   [自動連結](#autolink)



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

