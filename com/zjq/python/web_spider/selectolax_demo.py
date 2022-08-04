# 使用 selectolax 提取页面p标签的内容，代码如下：

# -*- coding: UTF-8 -*-
from selectolax.parser import HTMLParser


def get_p(html):
    p_list = []
    for node in HTMLParser(html).css("p"):
        # 提取代码
        p_list.append(node.text())
    return p_list


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

    print(get_p(html))
