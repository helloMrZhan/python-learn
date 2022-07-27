# 便利的 Python 计时器，统计从 0 遍历到 100000 消耗的时间，精确到毫秒

from datetime import datetime
from time import time, mktime

class TimeSpan:
    def __init__(self) -> None:
        self.start = round(time() * 1000)

    # 在此计算从开始到现在的耗时，精确到毫秒
    def elapse_mill_secs(self):
        end = round(datetime.now().timestamp() * 1000)
        return end - self.start

    # def elapse_mill_secs(self):
    #     end = round(time() * 1000)
    #     return end - self.start

    # def elapse_mill_secs(self):
    #     end = round(mktime(datetime.now().timetuple()) * 1000)
    #     return end - self.start


    def elapse_secs(self):
        return (self.elapse_mill_secs())/1000

if __name__ == '__main__':
    s = TimeSpan()

    for i in range(0, 100000):
        pass
    print('耗时： {} 毫秒'.format(s.elapse_mill_secs()))
    print('耗时： {} 秒'.format(s.elapse_secs()))