# Let's try to draw a point moving on a line
# To make things simple, we are going back to 1D

pos = 1
velo = 1

# Since there are multiple positions at a time, we can represent as a list
line_1 = [' ', ' ', ' ']
line_2 = 3*[' ']

# Note how they are equal statements
print(line_1, line_2)

# If we wanted to print the line without the list notation
# We can join an empty string with a list
print("".join(line_1))