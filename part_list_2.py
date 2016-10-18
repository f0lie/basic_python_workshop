# Tuples are immutable
# You cannot change them once you define them
# Meaning that if pos is a tuple, we can't update the pos

# But we can fix that with lists
pos = [0,0]
velo = [1,1]

print(pos, velo)

# Much like tuples, we get numbers by indexing
print(pos[0])
print(pos[1])

# Now we can modify pos as a pair of numbers
# Unforturately its not very readable
for i in range(10):
    print(pos)
    pos[0] += velo[0]
    pos[1] += velo[1]

print(pos)
