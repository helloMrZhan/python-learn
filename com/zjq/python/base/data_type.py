

if __name__ == '__main__':
    # 字符串
    print("字符串加法" + "字符串加法")
    print("字符串乘法" * 3)
    print(",".join(["字符串数组的聚合", "字符串数组的聚合", "字符串数组的聚合"]))

    print("双引号字符串")
    print('单引号字符串')
    triple = '''三引号字符串'''
    print("双引号字符串里的单引号: 'hello world!'")
    print('单引号字符串里的双引号: "hello world!"')

    # 列表
    array = []
    array.append(10)
    array.append(20)
    array.pop(0)
    array.append(30)
    array.append(40)
    array.pop(0)

    # 元数组
    tuple = ('红色', '绿色', '蓝色')
    for element in tuple:
        print(element)

    import math
    r, g, b = 0.6, 0.8, 0.3
    hr, hg, hb = (math.pow(r, 3 / 2), math.pow(g, 4 / 5), math.pow(b, 3 / 2))
    print("使用《黑客帝国》绿色滤镜算法计算后的颜色[0-1]：({}, {}, {})".format(hr, hg, hb))

    print("不带括号的也是元组:")
    r, g, b = 0.6, 0.8, 0.3
    print("普通颜色[0-1]：({}, {}, {})".format(r, g, b))

    # 字典（等同于java中的map）
    map = {}
    map['name'] = "monkey"
    map['age'] = 25
    map['tags'] = "猴子"
    map['tags'] = ['程序员', '户外达人']
    map['profile'] = {'info1': "test", "info2": "test"}

    print(map['tags'])
    print(map['profile'].get("info3"))


