# requests post 请求

# -*- coding: UTF-8 -*-
import requests

# 在此实现代码
def get_response(url, data, headers=None):
    response = requests.post(url, data, headers)
    result = response.text
    return result

if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
    }
    data = {
        "key1": "value1",
        "key2": "value2"
    }
    url = "http://httpbin.org/post"
    html = get_response(url, data, headers)
    print(html)