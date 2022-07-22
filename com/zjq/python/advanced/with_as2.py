# 实现一个范围耗时统计类。 实现了 __enter__ 和 __exit__ 成员的类，可以通过 with as 语法使用，程序进入和离开范围的时候会自动调用 __enter__ 和 __exit__ 方法。

import time

# class TimeSpan:
#     def __enter__(self):
#         self.end = None
#         self.start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.end = time.time()
#         print('耗时:{}毫秒'.format((self.end-self.start)))

class TimeSpan:
    def __enter__(self):
        self.end = None
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print('耗时:{}毫秒'.format((self.end-self.start)))

class TimeSpan:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print('耗时:{}毫秒'.format((self.end-self.start)))

if __name__ == '__main__':
    with TimeSpan() as t:
        for i in range(0, 1000):
            print(i)