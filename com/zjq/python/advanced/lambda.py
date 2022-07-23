# Python 高阶函数编程，使用 lambda 表达式获取key，将list转成dict

# -*- coding: UTF-8 -*-
def list_to_dict(list, key_func):
    d = {}
    for item in list:
        k = key_func(item)
        v = item
        list = d.get(k)
        if list is None:
            d[k] = [v]
        else:
            d[k].append(v)

    return d


if __name__ == '__main__':
    list = [
        {"name": "alice", "age": 100},
        {"name": "middle", "age": 100},
        {"name": "bob", "age": 200}
    ]
    # 调用 list_to_dict 方法，将 list 转成dict
    # 方式一
    # def get_key(item):
    #     return item['age']
    # ret = list_to_dict(list, get_key)
    # 方式二
    # ret = list_to_dict(list, lambda item: item['age'])
    # 方式三
    get_key = lambda item: item['age']
    ret = list_to_dict(list, get_key)
    print(ret)
