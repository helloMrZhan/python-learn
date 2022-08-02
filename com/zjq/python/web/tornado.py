# Python tornado 框架
#
# tornado 服务，极简路由

# -*- coding: UTF-8 -*-
import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""

    def get(self):
        """对应http的get请求方式"""
        # 实现Tornado get 方法
        self.write("Hello Tornado!")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    app.listen(8000)

    print("* Tornado Web Server 已在 8000 端口启动。")
    print("* 请在浏览器里输入 127.0.0.1:8000")
    tornado.ioloop.IOLoop.current().start()