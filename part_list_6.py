# Lets attempt to draw two points and have them move also

pos_1 = 0
velo_1 = 1

pos_2 = 9
velo_2 = -1

line = 10*[' ']

for i in range(10):
    line[pos_1] = '*'
    line[pos_2] = '*'
    print("".join(line))
    line[pos_1] = ' '
    line[pos_2] = ' '

    pos_1 += velo_1
    pos_2 += velo_2

# Note that if we used the pos now to index the line, we would get errors or wrong behavior
print(pos_1, pos_2)
print("".join(line))

# This is going to become extremely problematic if we try to go beyond this
# If we wanted to add more points or dimensions, the code will quickly degrade`