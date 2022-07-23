# 'a.json'文件不存在，下面代码会有异常，请编写异常控制代码，控制异常的最小范围，出现异常正常打印日志和堆栈

# -*- coding: UTF-8 -*-
import json
import traceback
import logging

logger = logging.getLogger(__name__)


def load_json(file):
    with open(file, 'r') as f:
        return json.loads(f.read())


def test():
    try:
        ret = load_json('a.json')
        return {'err': 'success', 'result': ret}
    except Exception as e:
        logger.error(f"load json exception:{str(e)}")
        logger.error(traceback.format_exc())
        return {'err': 'exception'}

if __name__ == '__main__':
    test()