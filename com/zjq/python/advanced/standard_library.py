# sys, os, math, time, date
# 请在使用的时候查文档，例如日期文档：https://docs.python.org/zh-cn/3/library/datetime.html#datetime.datetime
import sys
import os
import math
import datetime
import time


if __name__ == '__main__':
    assert type(sys.argv) == type([])
    assert os.path.exists(__file__) == True
    assert math.pow(2, 3) == 8
    assert type(time.time()) == type(2.3)
    assert datetime.now().year >= 2021

# json序列化与反序列化
import json
if __name__ == '__main__':
    # 在此实现json序列化和反序列化代码
    obj = json.loads(json.dumps({"key": {"items": [1, 2, "test"]}}))
    assert obj['key']['items'][2] == "test"
