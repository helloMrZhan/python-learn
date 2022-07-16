def test():
    print("* 如果想计算一个长方形的面积")
    print("* 那就先定义长宽，例如：x = 10, y=20")
    print("* 紧接着，我们计算长方形的面积：s = x * y")

    x = 10
    y = 20
    s = x * y

    print("* 现在可以输出结果了，该长方形的面积是：{}".format(s))

if __name__ == '__main__':
    test()