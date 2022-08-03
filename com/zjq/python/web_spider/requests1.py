# 获取url对应的网页HTML

# -*- coding: UTF-8 -*-
import requests

# 在此实现代码
def get_html(url):
    response = requests.get(url=url)
    result = response.text
    return result

if __name__ == '__main__':
    url = "http://www.baidu.com"
    html = get_html(url)
    print(html)