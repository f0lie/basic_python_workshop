# We can represent the concept of a point with a class
# We have multiple variables assoicated with a point
# Every point has a x and velo
class Point():
    def __init__(self, x, velo):
        self.x = x
        self.velo = velo

    def move(self):
        self.x += self.velo

    def print(self):
        print(self.x, self.velo)

line = 10*[' ']

point = Point(0,1)

for i in range(10):
    line[point.x] = '*'
    print("".join(line))
    line[point.x] = ' '
    point.move()

point.print()