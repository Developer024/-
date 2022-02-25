#!/usr/bin/python
# @developer024 July 3
# -*- coding: UTF-8 -*-
import requests
import datetime
import json

url = "http://www.zhonghuanus.com/integral/onclickSign"
Login_url = "http://www.zhonghuanus.com/webLogin"
FT_URL = "https://sctapi.ftqq.com/SCT49557TZrX7sPFjlsCMc6j2qaZfuC5V.send?"

#自动登录获取Cookie的Session
payload = json.dumps({
  "username": "admin",
  "password": "admin",
  "loginType": 1
})
headers = {
  'Host': 'www.zhonghuanus.com',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'X-Requested-With': 'XMLHttpRequest',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
  'Content-Type': 'application/json',
  'Origin': 'http://www.zhonghuanus.com',
  'Referer': 'http://www.zhonghuanus.com/dologin'
}
res = requests.request("POST", Login_url, headers=headers, data=payload)
res_dic = requests.utils.dict_from_cookiejar(res.cookies) #从cookiejar转化到字典类型
session = res_dic["SESSION"]
duid = res_dic["__yjs_duid"]

#处理自动签到模块
NowDate =  datetime.date.today() #当前的日期
StrNowdate = NowDate.strftime("%Y%m%d") 
payload = "date="+StrNowdate
Cookies = "__yjs_duid="+ duid + ";SESSION=" + session
headers = {
  'Host': 'www.zhonghuanus.com',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Referer': 'http://www.zhonghuanus.com/integral/signin',
  'Cookie': Cookies
}
response = requests.request("POST", url, headers=headers, data=payload)
#处理自动推送模块
SucessNotice = json.loads(response.text) #提取文字
FinalSucessNotice = SucessNotice["msg"]
title= "中环转运签到通知"
desp="Ding"
data1={
  "title": "中环转运签到通知",
  "desp": FinalSucessNotice
}
Notice = requests.request("POST", FT_URL, data=data1)

print(FinalSucessNotice)