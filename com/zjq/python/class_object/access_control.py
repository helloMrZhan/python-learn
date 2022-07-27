# 分别编写类内部的私有方法，模块级别的私有方法
class Test:
    def test(self):
        self.__test()

    def __test(self):
        '''类内部的私有方法'''
        print("test")

def _func():
    '''模块级别的私有方法'''
    print("file private")

if __name__ == '__main__':
    t = Test()
    t.test()