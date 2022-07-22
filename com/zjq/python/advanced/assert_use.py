# 所谓断言，就是证明，使用 assert 对输入函数输入参数和函数返回结果分别做前校验和后校验

def check_param(key_value_map, key):
    '''参数校验，断言就是对输入参数的一个证明，这些参数必须符合这些要求
    key_value_map: 非空字典
    key：非空字符串
    '''
    #方式1
    # assert key_value_map is not None
    # assert type(key_value_map) == type({})
    # assert key is not None
    # assert type(key) == type("")
    # 方式2
    assert key_value_map is not None and type(key_value_map) == type({})
    assert key is not None and type(key) == type("")
    # 方式3
    assert key_value_map is not None
    assert type(key_value_map) == dict
    assert key is not None
    assert type(key) == str

def get(key_value_map, key):
    check_param(key_value_map, key)
    return key_value_map.get(key)

def set(key_value_map, key, value):
    check_param(key_value_map, key)
    key_value_map[key] = value

if __name__ == '__main__':
    key_value_map = {}
    set(key_value_map, "test", {})
    value = get(key_value_map, "test")
    print("后校验，返回值必须符合预期")
    assert type(value) == type({})
    assert value == {}