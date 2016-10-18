class Point():
    def __init__(self, x=0, velo=0):
        self.x = x
        self.velo = velo

    def move(self):
        self.x += self.velo

    def print(self):
        print(self.x, self.velo)

class Line():
    def __init__(self, size, points=None):
        if points is None:
            self.points = []
        self.line = size*[' ']
        self.points = points

    def print(self):
        for point in self.points:
            self.line[point.x] = '*'
            
        print("["+"".join(self.line)+"]")
        
        for point in self.points:
            self.line[point.x] = ' '

points = [Point(0,1)]
line = Line(10, points)

for i in range(10):
    line.print()
    for point in points:
        point.move()