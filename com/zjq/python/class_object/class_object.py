# 创建学生类, 创建一个学生列表，加入3个学生，循环打印学生信息
# 方式一
class Student:
    # 初始化成员
    def __init__(self, no, name, age):
        self.no = no
        self.name = name
        self.age = age

    # 打印信息
    def dump(self):
        infos = [
            f"* no:{self.no}",
            f"* name:{self.name}",
            f"* age:{self.age}"
        ]
        for info in infos:
            print(info)

# 方式二
# class Student:
#     def __init__(self, no, name, age):
#         self.no = no
#         self.name = name
#         self.age = age
#
#     def dump(self):
#         print(f"* no:{self.no}")
#         print(f"* name:{self.name}")
#         print(f"* age:{self.age}")

# 方式三
# class Student:
#     def __init__(self, no, name, age):
#         self.fields = {
#             'no': no,
#             'name': name,
#             'age': age
#         }
#
#     def dump(self):
#         for field_name in self.fields:
#             field_value = self.fields[field_name]
#             print(f'* {field_name}:{field_value}')

if __name__ == '__main__':
    students = []
    for i in range(0, 3):
        s = Student(i, f'somebody_{i}', 20+i)
        students.append(s)

    for s in students:
        print('')
        s.dump()