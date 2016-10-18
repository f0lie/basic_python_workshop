class Point():
    def __init__(self, x, velo):
        self.x = x
        self.velo = velo

    def move(self):
        self.x += self.velo

    def print(self):
        print(self.x, self.velo)

line = 10*[' ']

point_1 = Point(0,1)
point_2 = Point(9,-1)

for i in range(10):
    line[point_1.x] = '*'
    line[point_2.x] = '*'
    print("".join(line))
    line[point_1.x] = ' '
    line[point_2.x] = ' '

    # We can represent behaviors with classes too
    # note how its more readible
    point_1.move()
    point_2.move()
    

point_1.print()
point_2.print()
