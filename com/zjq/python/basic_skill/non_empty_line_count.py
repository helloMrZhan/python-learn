# 统计文件中行数，非空行数，以及空格间隔的token数

# -*- coding: UTF-8 -*-
import json

def count_file(file):
    line_count = 0
    non_empty_line_count = 0
    token_count = 0

    with open(file, 'r') as f:
        while True:
            # 读取每行
            line = f.readline()
            if not line:
                break

            line_count += 1
            line_len = len(line)
            line_token_count = 0

            # 实现统计单行token数
            blank = False
            for char in line:
                if char in [' ', '\t', '\b']:
                    blank = True
                else:
                    if blank:
                        line_token_count += 1
                    blank = False

            token_count += line_token_count
            if line_token_count > 0:
                non_empty_line_count += 1

    return {
        'file': file,
        'line_count': line_count,
        'line_token_count': token_count,
        'non_empty_line_count': non_empty_line_count
    }

if __name__ == '__main__':
    ret = count_file('count_file.py')
    print('行数：', ret['line_count'])
    print('非空行：', ret['non_empty_line_count'])
    print('非空词数：', ret['line_token_count'])
    with open('/tmp/count.json', 'w') as f:
        f.write(json.dumps(ret, indent=2, ensure_ascii=False))