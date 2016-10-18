class Point():
    def __init__(self, x, velo):
        self.x = x
        self.velo = velo

line = 10*[' ']

# We can easily add more than one point while keeping it readible 
point_1 = Point(0,1)
point_2 = Point(9,-1)

# point_1 and point_2 have the same attitude yet they are different
for i in range(10):
    line[point_1.x] = '*'
    line[point_2.x] = '*'
    print("".join(line))
    line[point_1.x] = ' '
    line[point_2.x] = ' '

    point_1.x += point_1.velo
    point_2.x += point_2.velo
    

print(point_1.x, point_1.velo)
print(point_2.x, point_2.velo)
