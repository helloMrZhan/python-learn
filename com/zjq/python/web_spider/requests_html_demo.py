# requests-html可以使爬虫开发人员方便的编写爬虫代码
# 使用 requests-html 提取页面https://www.baidu.com/上面的所有链接，代码如下：

# -*- coding: UTF-8 -*-
from requests_html import HTMLSession

def get_url(url):
    session = HTMLSession()
    r = session.get(url)
    # 提取代码
    urls = r.html.links
    return urls

if __name__ == '__main__':
    print(get_url("https://www.baidu.com/"))