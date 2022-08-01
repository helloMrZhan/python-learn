# Python Web 服务模拟器
#
# 综合使用前2节的ErrorCode、Router两个类，模拟一个 Web 服务，支持：
#
# 创建资源
# 删除资源
# 统计资源个数
# 那么，先创建一个资源，接着删除同一个资源，最后统计资源个数，总数应该为0

# -*- coding: UTF-8 -*-
from error_code import ErrorCode
from store import Store
from router import Router
from validator import KeyValueValidator
import json
import logging
import traceback
logger = logging.getLogger(__name__)

class App:
    def __init__(self) -> None:
        self.store = Store({})
        self.validator = KeyValueValidator()

        # 创建一个路由器，支持3个目标API
        self.router = Router({
            '/': lambda req: self.__home(req),
            '/kv/create': lambda req: self.__create(req),
            '/kv/remove': lambda req: self.__remove(req),
            '/kv/count': lambda req: self.__count(req),
        })


    # 请正确实现 post 方法，接受 API 请求
    def post(self, path, data):
        '''HTTP POST方法模拟实现
        path: 请求路径
        data: 请求数据，使用JSON模拟
        '''
        http_request = {
            'path': path,
            'data': data
        }
        ret, status_code = self.router.dispatch(json.dumps(http_request))
        ErrorCode.internal_ret_2_http(ret)
        resp = ""
        try:
            resp = json.dumps(ret)
        except Exception as e:
            logger.error("parse resp exception:%s", str(e))
            logger.error(traceback.format_exc())
        return resp, status_code

    def __home(self, req):
        # 首页
        return {'err': ErrorCode.SUCCESS, 'result': "Welcome!"}

    def __create(self, req):
        # 创建资源
        ret = self.validator.validate(req, ['key', 'value'])
        if ret['err'] != ErrorCode.SUCCESS:
            return ret

        return self.store.create(req['key'], req['value'])

    def __remove(self, req):
        # 移除资源
        ret = self.validator.validate(req, ['key', 'condition'])
        if ret['err'] != ErrorCode.SUCCESS:
            return ret

        return self.store.remove(req['key'], req['condition'])

    def __count(self, req):
        # 统计资源个数
        return self.store.count()


if __name__ == '__main__':
    app = App()

    resp, status = app.post('/kv/create', {
        'key': 'test',
        'value': 1000,
    })

    resp, status = app.post('/kv/remove', {
        'key': 'test',
        'condition': 1000,
    })

    resp, status = app.post('/kv/count', {})
    assert status == 200
    assert json.loads(resp)['err'] == 'success'
    assert json.loads(resp)['result'] == 0