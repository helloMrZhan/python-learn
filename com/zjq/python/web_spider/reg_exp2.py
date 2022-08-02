# 返回匹配到的第一个

# -*- coding: UTF-8 -*-
import re

def search_text(inputdata):
    '''search返回匹配到的一个'''
    # 在此实现代码
    chi = re.search('nlp', inputdata)
    return chi

def test():
    n = search_text('你好，nlp先生！nlp先生！')
    print(n)

if __name__ == '__main__':
    test()