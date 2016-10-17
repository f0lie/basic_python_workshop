pos = 0
velo = 1

# We can repeat statements with for loops
# range(10) represents a sequence of numbers start at 0 and ending at 9 
# Python assigns the value into i as it moves through the sequence
for i in range(10):
    print(pos, i)
    pos += velo
# There is also an effect of increased readability

# This is the final value of pos
print(pos, i)