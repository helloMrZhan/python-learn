# 下面是People、Student和Teacher三个类

class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student:
    def __init__(self, no, name, age):
        self.name = name
        self.age = age
        self.no = no

class Teacher:
    def __init__(self, access_key, name, age):
        self.name = name
        self.age = age
        self.access_key = access_key

if __name__ == '__main__':
    s = Student(0, f'somebody', 20)
    t = Teacher('jladfja', 'linus', 0)

    print('# 教师')
    print(f"* name:{t.name}")
    print(f"* age:{t.age}")
    print('')
    print('# 学生')
    print(f"* no:{s.no}")
    print(f"* name:{s.name}")
    print(f"* age:{s.age}")

# 实际上Student 和 Teacher 可以从 People 类继承，复用实现
# class Student(People):
#     def __init__(self, no, name, age):
#         super().__init__(name, age)
#         self.no = no
#
# class Teacher(People):
#     def __init__(self, access_key, name, age):
#         super().__init__(name, age)
#         self.access_key = access_key