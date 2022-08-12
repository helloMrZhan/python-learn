from datetime import datetime, timedelta

if __name__ == '__main__':
    today = datetime.now()
    print(today)
    print(today.strftime("%d/%m/%y"))
    print(today.strftime("%A %d %B %Y"))

    # 在此计算昨天和明天日期
    # yesterday = today + timedelta(weeks=0, days=-1)
    # nextday = today + timedelta(weeks=0, days=1)

    yesterday = today - timedelta(days=1)
    nextday = today - timedelta(days=-1)

    # yesterday = today + timedelta(days=-1)
    # nextday = today + timedelta(days=1)
    print(yesterday)
    print(nextday)

    # # 时间字符串转时间戳
    # import time
    # today = "2022-08-12 08:08:08"
    # timearray = time.strptime(today, "%Y-%m-%d %H:%M:%S")
    # timeStamp = int(time.mktime(timearray))
    # print(timeStamp)