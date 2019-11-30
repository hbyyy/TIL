from collections import namedtuple

Point = namedtuple('Point', 'y z')

pt1 = Point(1.0, 2.0)
print(pt1)
print(type(pt1))