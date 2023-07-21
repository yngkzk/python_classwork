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

    def add(self, point1, point2):
        new_point = [point1, point2]
        self.points.append(new_point)


triangle = Figure()
triangle.add(Point(5, 8))
