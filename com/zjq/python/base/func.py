# -*- coding: UTF-8 -*-
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

if __name__=='__main__':
    dump(0)
    dump(0,2)
    dump(0,2,"Hello","World")
#    dump(0,2,"Hello","World", install='Python', run='Python Program')


# 递归调用
def circulate_print(str, count=0):
    if count == 5:
        return
    for char in str:
        print(char)
        circulate_print(str, count + 1)


if __name__ == '__main__':
    str = "Hello,World!"
    circulate_print(str)