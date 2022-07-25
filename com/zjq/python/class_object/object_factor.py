############# 封装 #################
# 使用类的方法获取相关信息，可以将内部的实现细节封装起来
# 封装写法1
# class Student:
#     def __init__(self, no, name, age):
#         self._no = no
#         self._name = name
#         self._age = age
#
#     def no(self):
#         return self._no
#
#     def name(self):
#         return self._name
#
#     def age(self):
#         return self._age

# 封装写法2
# class Student:
#     def __init__(self, no, name, age):
#         self.info =[no, name, age]
#
#     def no(self):
#         return self.info[0]
#
#     def name(self):
#         return self.info[1]
#
#     def age(self):
#         return self.info[2]

# 封装写法3
class Student:
    def __init__(self, no, name, age):
        self.info = {
            'no': no,
            'name': name,
            'age': age
        }

    def no(self):
        return self.info['no']

    def name(self):
        return self.info['name']

    def age(self):
        return self.info['age']

if __name__ == '__main__':
    s = Student(0, f'somebody', 20)
    print(f'* {s.no()}')
    print(f'* {s.name()}')
    print(f'* {s.age()}')