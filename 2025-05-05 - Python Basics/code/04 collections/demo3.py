# create a list of 25 random numbers in the range 100 - 200
# print the list
import random

numbers = []
print(numbers)
# add 25 random numbers

c = 1

while c <= 25:
    r = random.randrange(100, 201)
    numbers.append(r) # add a new element to the list
    # print(numbers)
    c = c + 1

print(numbers)


