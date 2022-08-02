# urlib 获取网页(1)
#
# 将 url 对应的网页下载到本地

import urllib.request


def get_html(url):
    response = urllib.request.urlopen(url)
    buff = response.read()
    html = buff.decode("utf8")
    return html

if __name__ == '__main__':
    url = "http://www.baidu.com"
    html = get_html(url)
    print(html)