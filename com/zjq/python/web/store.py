# 状态存储
# 使用dict数据结构，实现创建、删除、查询总数存储接口，创建/删除同一个资源后，总是应该为0

# -*- coding: UTF-8 -*-
from error_code import ErrorCode
import logging
logger = logging.getLogger(__name__)

class Store:
    def __init__(self, config) -> None:
        self.config = config
        self.records = {}

    def __where(self, key, condition):
        if condition is None:
            return True
        return self.records.get(key) == condition

    def create(self, key, value):
        if self.records.get(key) is None:
            self.records[key] = value
            return {'err': ErrorCode.SUCCESS}
        else:
            return {'err': ErrorCode.ALREADY_EXIST}

    def update(self, key, value, condition=None):
        if self.__where(key, condition):
            self.records[key] = value
            return {'err': ErrorCode.SUCCESS}
        else:
            return {'err': ErrorCode.NOT_FOUND}

    def remove(self, key, condition=None):
        if self.__where(key, condition):
            del self.records[key]
            return {'err': ErrorCode.SUCCESS}
        else:
            return {'err': ErrorCode.NOT_FOUND}

    def count(self):
        return {'err': ErrorCode.SUCCESS, 'result': len(self.records.keys())}

    # 请实现一个根据key 和条件 condition 查找的方法
    def fetch(self, key, condition=None):
        if self.__where(key, condition):
            result = self.records.get(key)
            if result is None:
                return {'err': ErrorCode.NOT_FOUND}
            else:
                return {'err': ErrorCode.SUCCESS, 'result': [result]}
        else:
            return {'err': ErrorCode.NOT_FOUND}


if __name__ == '__main__':
    store = Store({})
    ret = store.create("test",  100)
    assert ret['err'] == ErrorCode.SUCCESS

    ret = store.remove("test")
    assert ret['err'] == ErrorCode.SUCCESS
    ret = store.count()
    assert ret['err'] == ErrorCode.SUCCESS
    assert ret['result'] == 0