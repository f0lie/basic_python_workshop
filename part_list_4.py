pos = 0
velo = 1

line = 10*[' ']

# We can use the index of an line as the positions on the line
# We can do so by using pos as a index for line
# And we can represent a point with *
for i in range(10):
    print("".join(line))
    line[pos] = '*'
    pos += velo

print(pos)
print("".join(line))

# But we have a problem
# By the end of the loop, "ten" points are drawn when in fact we wanted only "one" to move