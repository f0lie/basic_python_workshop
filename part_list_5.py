pos = 0
velo = 1

line = 10*[' ']

for i in range(10):
    # We draw a point on the line and erase it after printing it
    line[pos] = '*'
    print("".join(line))
    line[pos] = ' '

    pos += velo

# Now we have drawn a point moving through a line
# Thou the line at the end is end
print(pos)
print("".join(line))
