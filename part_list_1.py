# We can represent related variables in a more compact way with tuples
pos = (0,0)
velo = (1,1)

print(pos, velo)

# We can get the first and second numnbers with indexes
print(pos[0])
print(pos[1])

# However, there is a problem...
for i in range(10):
    pos[0] += velo[0]
    pos[1] += velo[1]

print(pos)