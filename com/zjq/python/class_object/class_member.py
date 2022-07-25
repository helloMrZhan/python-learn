# 类成员变量可以直接访问，直接调用学生类的成员变量，打印学生信息

# 普通初始化函数添加成员
class Student:
    # 实现含有no/name/age 三个成员属性的学生类
    # 实现方式一
    def __init__(self, no, name, age):
        self.no = no
        self.name = name
        self.age = age
# 实现方式二
# 使用 @dataclass 可以简化实现
# from dataclasses import dataclass
#
# @dataclass
# class Student:
#     no: int
#     name: str
#     age: int

# 实现方式三
# # 使用 @dataclass + slot 可以简化实现并且优化内存占用
# from dataclasses import dataclass
#
# @dataclass
# class Student:
#     __slots__ = ['no', 'name', 'age']
#     no: int
#     name: str
#     age: int

def test():
    students = []
    for i in range(0, 3):
        s = Student(i, f'somebody_{i}', 20+i)
        students.append(s)

    for s in students:
        print('')
        print(f"* no:{s.no}")
        print(f"* name:{s.name}")
        print(f"* age:{s.age}")

if __name__ == '__main__':
    test()