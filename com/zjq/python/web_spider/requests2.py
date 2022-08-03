# 将url对应的网页下载到本地

# -*- coding: UTF-8 -*-
import requests

def get_html(url, headers=None):
    response = requests.get(url=url)
    return response.text

if __name__ == '__main__':
    # 正确编写 headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
    }
    url = "http://www.baidu.com"
    html = get_html(url, headers)
    print(html)