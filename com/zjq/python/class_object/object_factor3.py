# Student 和 Teacher 类都继承 People 类。Student 和 Teacher 类可以动态改变 People 类的 infos 方法，添加子类新增信息。程序入口可以对它们统一处理，打印他们的基本信息

class People:
    def __init__(self, role, name, age):
        self.name = name
        self.age = age
        self.role = role

    def infos(self):
        return [
            f"name:{self.name}",
            f"age:{self.age}",
            f"role:{self.role}"
        ]

class Student(People):
    def __init__(self, no, name, age):
        super().__init__("student", name, age)
        self.no = no

    def infos(self):
        info_list = super().infos()
        info_list.append(f'no:{self.no}')
        return info_list


class Teacher(People):
    def __init__(self, access_key, name, age):
        super().__init__("teacher", name, age)
        self.access_key = access_key

    def infos(self):
        info_list = super().infos()
        info_list.append(f'access_key:{self.access_key}')
        return info_list


if __name__ == '__main__':
    peoples = [
        Teacher("ajladfjkadf", "Linus", 0)
    ]

    for i in range(0, 3):
        s = Student(i, f'somebody_{i}', 20+i)
        peoples.append(s)

    for p in peoples:
        print()
        for info in p.infos():
            print(info)

