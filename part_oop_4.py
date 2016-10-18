class Point():
    def __init__(self, x, velo):
        self.x = x
        self.velo = velo

    def move(self):
        self.x += self.velo

    def print(self):
        print(self.x, self.velo)

# You can have lists as attitude too
class Line():
    def __init__(self, size, points=None):
        self.line = size*[' ']

        # There is a very techanical reason for this but its out of the scope of the workshop
        if points is None:
            self.points = []
        self.points = points

# We store points in a list within list so its easier to add more points
line = Line(10, [Point(0,1), Point(9,-1)])

# While the code is a bit noiser, the intents are clear
for i in range(10):
    # We can directly loop over items in a list without having to deal with indexes
    for point in line.points:
        line.line[point.x] = '*'
    print("".join(line.line))
    for point in line.points:
        line.line[point.x] = ' '

    for point in line.points:
        point.move()

for point in line.points:
    point.print()

