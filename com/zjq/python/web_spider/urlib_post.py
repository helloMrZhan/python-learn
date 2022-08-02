# urllib post请求
#
# urllib post请求

import urllib.request
import urllib.parse

# 在此编写代码
def get_response(url, data):
    data = bytes(urllib.parse.urlencode(data), encoding='utf8')
    response = urllib.request.urlopen(
        url, data=data
    )
    buff = response.read()
    result = buff.decode("utf8")
    return result

if __name__ == '__main__':
    data = {
        "key1": "value1",
        "key2": "value2"
    }
    url = "http://httpbin.org/post"
    html = get_response(url, data)
    print(html)