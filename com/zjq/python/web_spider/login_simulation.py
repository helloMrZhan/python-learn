# 以下是一个使用 cookie 模拟登录请求页面的例子

# -*- coding: UTF-8 -*-
import requests
import sys
import io

if __name__ == "__main__":
    # 登录后才能访问的网页
    url = 'http://www.csdn.net'

    # 浏览器登录后得到的cookie
    cookie_str = r'xxx=yyy;zzz=mmm'

    # 把cookie字符串处理成字典，以便接下来使用
    # 准备cookie数据
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value

    # 设置请求头
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }

    # 在发送get请求时带上请求头和cookies
    resp = requests.get(
        url,
        headers=headers,
        cookies=cookies
    )

    print(resp.content.decode('utf-8'))