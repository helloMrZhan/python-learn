# 创建点对象，有多种方式创建一个类的实例，我们称一个点的x、y、z都一样的点为对角点。

# 添加类静态方法，批量创建对角点
# class Point:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     @staticmethod
#     def create_diag_points(count):
#         points = []
#         for i in range(count):
#             points.append(Point(i,i,i))
#         return points
#
# if __name__ == '__main__':
#     points = Point.create_diag_points(1000)

# 通过 @classmethod 装饰器，增加一个类级别的创建方法，批量创建
# class Point:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     @classmethod
#     def create_diag_points(cls, count):
#         # 在@classmethod修饰的方法中，其中 cls 表示 Point
#         points = []
#         for i in range(count):
#             points.append(cls(i,i,i))
#         return points
#
# if __name__ == '__main__':
#     points = Point.create_diag_points(1000)

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

if __name__ == '__main__':
    points = []
    for i in range(1000):
        points.append(Point(i,i,i))