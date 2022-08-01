
# 路由器
#
# 下面是一个 HTTP 状态代码的定义：
#
# 2xx：成功:
#
# 200 正常，请求已完成。
# 201 正常，紧接POST命令。
# 202 正常，已接受用于处理，但处理尚未完成。
# 203 正常，部分信息—返回的信息只是一部分。
# 204 正常，无响应—已接收请求，但不存在要回送的信息。

# 3xx：重定向:
#
# 301 已移动，请求的数据具有新的位置且更改是永久的。
# 302 已找到，请求的数据临时具有不同 URI。
# 303 请参阅其它，可在另一 URI 下找到对请求的响应，且应使用 GET 方法检索此响应。
# 304 未修改，未按预期修改文档。
# 305 使用代理，必须通过位置字段中提供的代理来访问请求的资源。
# 306 未使用，不再使用，保留此代码以便将来使用。

# 4xx：客户机中出现的错误:
#
# 400 错误请求，请求中有语法问题，或不能满足请求。
# 401 未授权，未授权客户机访问数据。
# 402 需要付款，表示计费系统已有效。
# 403 禁止，即使有授权也不需要访问。
# 404 找不到，服务器找不到给定的资源；文档不存在。
# 407 代理认证请求，客户机首先必须使用代理认证自身。
# 415 介质类型不受支持，服务器拒绝服务请求，因为不支持请求实体的格式。

# 5xx：服务器中出现的错误:
#
# 500 内部错误，因为意外情况，服务器不能完成请求。
# 501 未执行，服务器不支持请求的工具。
# 502 错误网关，服务器接收到来自上游服务器的无效响应。
# 503 无法获得服务，由于临时过载或维护，服务器无法处理请求。
# 编写一个路由服务，支持注入路由配置，正确处理请求参数

# -*- coding: UTF-8 -*-
from error_code import ErrorCode
import json
import logging
import traceback
logger = logging.getLogger(__name__)

class Router:
    def __init__(self, routes) -> None:
        self.routes = routes

    # 请实现路由逻辑，返回符合语义的HTTP状态码
    def dispatch(self, http_request_str):
        req_path = None
        req = None
        try:
            http_request = json.loads(http_request_str)
            req_path = http_request.get('path')
            req = http_request.get('data')
        except Exception as e:
            logger.error(f"parse data exception:{str(e)}")
            return {'err': ErrorCode.INVALID_PARAMETERS}, 400

        if req_path is None or self.routes.get(req_path) is None:
            return {'err': ErrorCode.NOT_FOUND}, 404

        try:
            handler = self.routes.get(req_path)
            return handler(req), 200
        except Exception as e:
            logger.error(f"route to '{req_path}' exception:{str(e)}")
            logger.error(traceback.format_exc())
            return {'err': ErrorCode.FAILED}, 500

if __name__ == '__main__':
    # 注册路由
    router = Router({
        '/': lambda req: print(f'goto home:{str(req)}')
    })

    # 分发路由
    router.dispatch(json.dumps({
        'path': '/',
        'data': ["Hello", "World!"]
    }))