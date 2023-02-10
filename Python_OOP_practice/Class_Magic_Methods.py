import math

class Point2D:
    def __init__(self, x, y):    # Metoda magiczna czyli zaczynajaca sie od __ np. __init__.
        self.x = x
        self.y = y
        self.range = math.sqrt(x**2 + y**2)

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def __lt__(self, other):
        return self.range < other.range

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int(round(self.range, 0))

p1 = Point2D(2, 5)
p2 = Point2D(4, 5)
p3 = p1 + p2
print (p1 < p2)

print ( p1 == p2)

print (p1 == p1)

print (len(p3))
print (p3.range)