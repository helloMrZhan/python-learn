# 编写一个简易的 ECHO 服务机器人。满足：
#
# 客户端发送文本，服务端回复同样的文本，两边都打印各自收到的文本。
# 客户端支持用户输入'q' 退出。
# 客户端支持每次不大于 140 的文本输入，如果超出则提示重新输入。
# 客户端必须正确打印字符串。
# -*- coding: UTF-8 -*-
import socket
import sys

def echo_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('收到客户端请求:', addr)
            while True:
                data = conn.recv(1024)
                print('收到客户端数据:', str(data, 'utf8'))
                if not data:
                    break
                conn.sendall(data)

def echo_client(host, port, input_message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # 实现发送处理逻辑
        while True:
            msg = input_message("请输入信息[按q退出]：")
            if msg == 'q':
                break

            if len(msg) > 140:
                print("您的输入太长了～～，请重新输入！")
                continue

            msg_buffer = bytes(msg, 'utf-8')
            s.sendall(msg_buffer)

            data = s.recv(1024)
            print('收到服务端回包：', str(data, 'utf8'))

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 9999

    # 如果命令行指定了 'server' 参数，就启动服务端程序
    # 否则，启动客户端程序
    if len(sys.argv) > 1 and sys.argv[1] == 'server':
        echo_server(host, port)
    else:
        echo_client(host, port, lambda tip: input(tip))