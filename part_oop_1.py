# We can represent the concept of a point with a class
# We have multiple variables assoicated with a point
# Every point has a x and velo
class Point():
    def __init__(self, x, velo):
        self.x = x
        self.velo = velo

line = 10*[' ']

point = Point(0,1)

# Note how point has an assoicated x and velo
# We call the point's x with point.x
for i in range(10):
    line[point.x] = '*'
    print("".join(line))
    line[point.x] = ' '

    point.x += point.velo

print(point.x, point.velo)
