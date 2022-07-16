# 函数
def dump(index, default=0, *args, **kw):
    print('打印函数参数')
    print('---')
    print('index:', index)
    print('default:', default)
    for i, arg in enumerate(args):
        print(f'arg[{i}]:', arg)
    for key,value in kw:
        print(f'keyword_argument {key}:{value}')
    print('')


# 递归调用
def circulate_print(str, count=0):
    if count == 5:
        return
    for char in str:
        print(char)
        circulate_print(str, count + 1)

# 阶乘
def fact(n):
    r = 1
    for i in range(0, n):
        r *= (i + 1)
    return r

# 斐波那契(fibonacci)1

# def fibonacci(n):
#     return fibonacci_inner(n, 2, 1, 1)

def fibonacci_inner(n, m, r0, r1):
    if m == n:
        return r1
    return fibonacci_inner(n, m+1, r1, r0+r1)

# 斐波那契(fibonacci)2
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)


# 斐波那契(fibonacci)增加缓存
def fibonacci(n):
    return fibonacci_inner(n, {})

def fibonacci_inner(n, cache):
    if n == 1 or n == 2:
        return 1
    r = 0
    if cache.get(n) is not None:
        return cache[n]
    else:
        cache[n] = fibonacci_inner(n - 1, cache) + fibonacci_inner(n - 2, cache)
        return cache[n]

if __name__ == '__main__':

    # 函数
    # dump(0)
    # dump(0, 2)
    # dump(0, 2, "Hello", "World")
    # dump(0,2,"Hello","World", install='Python', run='Python Program')

    # 递归
    # str = "Hello,World!"
    # circulate_print(str)

    # 阶乘
    # print(fact(10))

    # 斐波那契(fibonacci) 数学家莱昂纳多·斐波那契（Leonardo Fibonacci）以兔子繁殖为例子引入了数列0、1、1、2、3、5、8、13、21、34...，称为斐波那契数列（Fibonacci sequence），又称“黄金分割数列”或者“兔子数列”。使用函数递归或非递归的方式都可以方便地计算斐波那契函数：F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 2）
    print(fibonacci(6))

