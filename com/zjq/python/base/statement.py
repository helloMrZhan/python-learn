# 顺序语句
def order():
    print("* 如果想计算一个长方形的面积")
    print("* 那就先定义长宽，例如：x = 10, y=20")
    print("* 紧接着，我们计算长方形的面积：s = x * y")

    x = 10
    y = 20
    s = x * y

    print("* 现在可以输出结果了，该长方形的面积是：{}".format(s))

# 条件语句
def condition():
    test = 10
    ret = input("有一个数除以2是5，请问它是什么？:")
    if ret == "{}".format(test):
        print("恭喜你答对了！")
    else:
        print("哎，这么简单都答不对，回去重修吧！")

# 条件语句2
def is_existed():
    database = {
        "monkey": "猴王说，我写的程序在五指山上的服务器上运行5000年了！"
    }
    key = input('请输入你要查询的关键字:')
    print("* 猴王数据库正在努力检索中...")
    if database.get(key) is None:
        print("* 无法检索到该信息！")
    else:
        print("* 返回：{}".format(database[key]))



if __name__ == '__main__':
    # order()
    # condition()
    # is_existed()

    # 使用 for 遍历打印列表信息
    list = [
        {
            "id": 966024429,
            "number": 2341,
            "title": "Question about license.",
            "body": "I would like to create a [winget](https://github.com/microsoft/winget-cli) package for jq. 🙏🏻"
        },
        {

            "id": 962477084,
            "number": 2340,
            "title": "visibility of wiki pages",
            "body": "The visibility of wiki pages to search engines is generally limited; for example, the search result for \"jq Cookbook\" looks like this:"
        }
    ]
    # 循环方式1
    i = 0
    for item in list:
        print('')
        print("## 第{}条信息".format(i))
        print("* id: {}".format(item['id']))
        print("* number: {}".format(item['number']))
        print("* title: {}".format(item['title']))
        print("* body: {}".format(item['body']))
        i += 1
    #循环方式2
    for i in range(len(list)):
        item = list[i]
        print('')
        print("## 第{}条信息".format(i))
        print("* id: {}".format(item['id']))
        print("* number: {}".format(item['number']))
        print("* title: {}".format(item['title']))
        print("* body: {}".format(item['body']))
    # 循环方式3
    for i, item in enumerate(list):
        print('')
        print("## 第{}条信息".format(i))
        print("* id: {}".format(item['id']))
        print("* number: {}".format(item['number']))
        print("* title: {}".format(item['title']))
        print("* body: {}".format(item['body']))

    # while循环方式1
    i = 0
    while i < len(list):
        item = list[i]
        print('')
        print("## 第{}条信息".format(i))
        print("* id: {}".format(item['id']))
        print("* number: {}".format(item['number']))
        print("* title: {}".format(item['title']))
        print("* body: {}".format(item['body']))
        i += 1

    # while循环方式2
    i = 0
    while True:
        item = list[i]
        print('')
        print("## 第{}条信息".format(i))
        print("* id: {}".format(item['id']))
        print("* number: {}".format(item['number']))
        print("* title: {}".format(item['title']))
        print("* body: {}".format(item['body']))
        i += 1
        if i == len(list):
            break
