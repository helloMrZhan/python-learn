# 发送QQ邮件

# -*- coding: UTF-8 -*-
import smtplib
import ssl
from email.mime.text import MIMEText

def test():
    sender = input("请输入你的QQ邮箱:")
    password = input("请输入你的QQ邮箱密码: ")
    receiver = input("请输入目标QQ邮箱:")
    content = input("请输入发送消息:")

    smtp_server = "smtp.qq.com"
    port = 465

    subject = "我在学习Python发送QQ邮件"
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        # 在此实现发送邮件代码
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
    except Exception as e:
        print("发送失败了")
        print(e)
        return {'err': 1}

    return {'err': 0}

if __name__ == '__main__':
    test()