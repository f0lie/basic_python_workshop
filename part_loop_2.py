# Now we define four variables to represent a point on the 2D plane
pos_x = 0
pos_y = 0

velo_x = 1
velo_y = 1

for i in range(10):
    print(pos_x, pos_y)
    pos_x += velo_x
    pos_y += velo_y

print(pos_x, pos_y)
