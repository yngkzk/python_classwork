''' Класс Point имеет свойства: x, y.
Класс Figure содержит массив точек (объектов класса Point) и методы:
        add(point) -- добавляет новую вершину к фигуре,
        perimeter() -- возвращает периметр фигуры.
    Реализовать эти классы.
'''


class Point:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Figure:
    x = Point.x
    y = Point.y
    points = []

    def add(self, point1=0, point2=0):
        new_point = [point1, point2]
        self.points.append(new_point)

    def perimeter(self):
        dist = 0
        for i in range(len(self.points)):
            dist += distance(self.points[i][0], self.points[i+1][1])
        return dist


def distance(point1, point2=None):
    if point2 is None:
        point2 = point1
        a2 = (point1.x - point2.x) ** 2
        b2 = (point1.y - point2.y) ** 2
        return (a2 + b2) ** 0.5
    else:
        a2 = (point1.x - point2.x) ** 2
        b2 = (point1.y - point2.y) ** 2
        return (a2 + b2) ** 0.5


def test_Point():
    p = Point(10, 20)
    assert p.x == 10 and p.y == 20

    p = Point()
    assert p.x == 0 and p.y == 0


def test_Figure():
    triangle = Figure()
    assert triangle.perimeter == 0

    triangle.add(Point(5, 5))
    assert triangle.perimeter == 0

    triangle.add(Point(8, 5))
    assert triangle.perimeter == 6

    triangle.add(Point(8, 8))
    assert triangle.perimeter == 6 + (9 + 9) ** 0.5

    triangle.add()
    assert triangle.perimeter == 6 + (9 + 9) ** 0.5


test_Point()
test_Figure()
