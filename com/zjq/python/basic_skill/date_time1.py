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