# 去除html标签

import re
from typing import Text

# 在此实现代码
def remove_html(content):
    pattern = re.compile(r'<[^>]+>', re.S)
    result = pattern.sub('', content)
    return result

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
    Text = remove_html(html)
    print(Text)