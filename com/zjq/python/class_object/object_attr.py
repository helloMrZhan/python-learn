class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Point3D:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

class Vector2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Vector3D:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

def test():
    points = [
        Point2D(0, 1),
        Point2D(0, 1),
        Point3D(0, 1, 2),
        Point3D(0, 1, 3),
        Vector2D(0, 1),
        Vector3D(0, 1, 4),
    ]

    z_objects = []
    # 过滤出含有'z'属性的对象，在过滤中打印出对应对象的'z'属性
    for p in points:
        if hasattr(p, 'z'):
            z = getattr(p, 'z')
            print('get z attr:', z)
            z_objects.append(p)

    for p in z_objects:
        print('x+y+z:', p.x+p.y+p.z)

if __name__ == '__main__':
    test()