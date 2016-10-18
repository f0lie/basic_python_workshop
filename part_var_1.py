# We have a line and we have a single point on it
# We can represent the point's position on the line with a variable
pos = 0

# The same with velocity
velo = 1

# We write the values into the terminal
print(pos, velo)

# If we want to represent speed, we add velo and pos together
pos += velo
print(pos)

# However, that would only increase the speed once
# If we wanted to increase the speed again, we add them together again
pos += velo
print(pos)

# But this is annoying to do