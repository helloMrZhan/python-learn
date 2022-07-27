import sys


def error(info):
    print(info)
    sys.exit(0)


def parse_option(token):
    if len(token) == 0 or len(token) == 1 or token[0] != '-':
        error("格式错误，选项长度至少大于2并且第一个字符必须是 '-'")

    if token[1] != '-':
        return token[1:]

    if len(token) == 2 or token[2] == '-':
        error("格式错误，不支持空选项 '--' 或则三横杆选项 '---x' ")

    return token[2:]


def parse_value(token):
    if token is None:
        return True

    if len(token) == 0:
        return True

    if token[0] == '-':
        error('格式错误')
    else:
        return token


if __name__ == '__main__':
    count = len(sys.argv)
    options = {}

    # 在此使用 parse_option 和 parse_value 解析命令行
    i = 1
    while i < count:
        token = sys.argv[i]
        next_token = None
        if i + 1 < count:
            next_token = sys.argv[i + 1]
            i = i + 1

        option = parse_option(token)
        value = parse_value(next_token)

        options[option] = value
        i += 1

    for option in options:
        value = options[option]
        print("{}={}".format(option, value))