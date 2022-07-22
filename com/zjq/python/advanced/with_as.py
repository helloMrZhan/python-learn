# JSON文件读写

import json

# 实现加载json文件代码
def load_json(file):
    with open(file, 'r') as f:
        return json.loads(f.read())

# 实现将dict写入json文件的代码
def dump_json(file, obj):
    with open(file, 'w') as f:
        f.write(json.dumps(obj, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    data = {
        'test': 1,
    }
    dump_json('test.json', data)
    load_json('test.json')