# 三元运算符

# 统计偶数
if __name__ == '__main__':
    pi = [3, 14, 15, 9, 26, 5, 35, 8, 97, 932]
    even_count = 0
    for i in pi:
        even_count += 1 if i % 2 == 0 else 0
    assert even_count == 4

# 使用嵌套的三元组表达式统计数字频率，如果是2的倍数加1，如果是4的倍数加2，否则加0
if __name__ == '__main__':
    pi = [3, 14, 15, 9, 26, 5, 35, 8, 97, 932]
    even_count = 0

    for i in pi:
        even_count += 2 if i % 4 == 0 else 1 if i % 2 == 0 else 0
    assert even_count == 6