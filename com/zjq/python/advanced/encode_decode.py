# 二进制只是二进制，取决于怎么编码和解码，unicode 转 utf8

# -*- coding: UTF-8 -*-
if __name__ == '__main__':
    unicode_str = u'二进制只是二进制，取决于怎么编码和解码'
    print(unicode_str)

    utf8_str = unicode_str.encode('utf-8')
    print(utf8_str)

    unicode_str_again = utf8_str.decode('utf-8')

    assert unicode_str_again == unicode_str