# API链路1
# def init():
#     return [], []
#
# def set(dict, key, value):
#     keys, values = dict
#     if not key in keys:
#         keys.append(key)
#         values.append(value)
#
# def get(dict, key):
#     keys, values = dict
#     if not key in keys:
#         return None
#     else:
#         return values[keys.index(key)]
#
# def exist(dict, key):
#     keys, values = dict
#     return key in keys

# API链路2
# def init():
#     return {}
#
# def set(dict, key, value):
#     dict[key] = value
#
# def get(dict, key):
#     return dict.get(key)
#
# def exist(dict, key):
#     return dict.get(key) is not None

# API链路3
def init():
    return []

def set(dict, key, value):
    if not key in dict or dict.index(key) % 2 != 0:
        dict.append(key)
        dict.append(value)

def get(dict, key):
    if key in dict:
        pos = dict.index(key)
        if pos % 2 == 0:
            return dict[pos+1]
    return None

def exist(dict, key):
    return key in dict and dict.index(key) % 2 == 0


if __name__ == '__main__':
    dict = init()
    for i in range(10):
        key = "key_{}".format(i)
        value = i
        set(dict, key, value)

    test_key = "key_4"
    if exist(dict, test_key):
        test_value = get(dict, test_key)
        print("key is: {}, value is: {}".format(test_key, test_value))