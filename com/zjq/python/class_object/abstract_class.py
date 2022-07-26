# 使用 abc 库，创建抽象 BasePoint 类，创建 Point 子类，实现 dot 抽象方法，计算内积

import abc

# 抽象类 BasePoint
class BasePoint:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    @abc.abstractmethod
    def dot(self, right):
        pass

class Point(BasePoint):
    def __init__(self, x, y, z) -> None:
        super().__init__(x, y, z)

    def dot(self, right):
        return self.x*right.x+self.y*right.y+self.z*right.z

if __name__ == '__main__':
    p1 = Point(0, 1, 2)
    p2 = Point(2, 4, 6)
    assert p1.dot(p2) == 16
    p1 = BasePoint(0, 1, 2)
    p2 = BasePoint(2, 4, 6)
    assert p1.dot(p2) is None