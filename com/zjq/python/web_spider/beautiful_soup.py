# 获取所有p标签里的文本

# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup

# 在此实现代码
def fetch_p(html):
    soup = BeautifulSoup(html, 'lxml')
    p_list = soup.find_all("p")
    results = [p.text for p in p_list]
    return results

if __name__ == '__main__':
    html = '''
        <html>
            <head>
                <title>这是一个简单的测试页面</title>
            </head>
            <body>
                <p class="item-0">body 元素的内容会显示在浏览器中。</p>
                <p class="item-1">title 元素的内容会显示在浏览器的标题栏中。</p>
            </body>
        </html>
        '''
    p_text = fetch_p(html)
    print(p_text)