# 获取中文个数

import re

def getnum_of_cn(inputdata):
    '''计算字符串中 中文字符 数量'''
    # 编写正则查询代码
    chi = re.findall(r'[\u4E00-\u9FFF]', inputdata)
    return len(chi)

def test():
    n = getnum_of_cn('你好，lajfldkjaklda123')
    print(n)

if __name__ == '__main__':
    test()