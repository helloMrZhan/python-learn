from datetime import date, timedelta
from calendar import monthrange

def next_month(d):
    # 在此实现计算下一个月的代码
    # 方式一
    # offset = monthrange(d.year, d.month)
    # first_weeky_day, days_in_month = offset
    # value = d + timedelta(days_in_month)
    # 方式二
    # days_in_month = monthrange(d.year, d.month)[1]
    # value = d + timedelta(days_in_month)
    # 方式三
    offset = monthrange(d.year, d.month)
    days_in_month = offset[1]
    value = d + timedelta(days_in_month)
    return value

def for_each_month(start, finish, action):
    while start < finish:
        action(start)
        start = next_month(start)

if __name__ == '__main__':
    for_each_month(
        date(2008, 1, 1),
        date.today(),
        lambda d: print(d)
    )