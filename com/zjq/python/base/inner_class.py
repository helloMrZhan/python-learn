#内置类的使用，列表元素去重+过滤小于3的元素

# 去重方式
def remove_duplicates(items):
    res = list(set(items))
    return res

# 过滤方式1
# def filter_element(items, bound):
#     res = [item for item in items if item < bound]
#     return res

# 过滤方式2
def filter_element(items, bound):
    res = [item for item in items if item < bound]
    return res


if __name__ == '__main__':
    a = [1, 2, 3, 4, 4, 5, 5]
    print('输入: {}'.format(a))

    res = remove_duplicates(a)
    print('去重后的结果：{}'.format(res))

    bound = 3
    res = filter_element(a, bound)
    print('过滤小于{}的元素:{}'.format(bound, res))