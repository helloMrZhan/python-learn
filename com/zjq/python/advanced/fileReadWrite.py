# 基本文件读写，写入 "test" 到 "/tmp/test.txt"，再次打开读取

if __name__ == '__main__':
    with open('/tmp/test.txt', 'w') as f:
        f.write("test")
    with open('/tmp/test.txt', 'r') as f:
        print(f.read())