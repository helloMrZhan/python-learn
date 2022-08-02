# 查找字符串里含有的全部IPV4和IPV6地址

import re


def find_all_ipv4(text):
    result = []
    ipv4 = r"((\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})"

    # 请在此匹配ipv4
    ret = re.findall(ipv4, text)

    for m in ret:
        result.append({'type': 'ipv4', 'value': m[0]})
    return result


def find_all_ipv6(text):
    result = []

    ipv6 = r"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"

    # 请在此匹配ipv6
    ret = re.finditer(ipv6, text)

    for m in ret:
        result.append({'type': 'ipv6', 'value': m[0]})
    return result


def find_all_ip(text):
    result = find_all_ipv4(text) + find_all_ipv6(text)
    return result


if __name__ == '__main__':
    input = 'IP地址有IPV4，例如：192.168.100.2，也有IPV6，例如：fe80:0000:0000:0000:0204:61ff:fe9d:f156，以及：fe80:0000:0000:0000:0204:61ff:fe9d:f156，还有 192.168.100.50'
    results = find_all_ip(input)
    for item in results:
        print('type: {}, value: {}'.format(item['type'], item['value']))