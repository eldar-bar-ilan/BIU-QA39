import random

my_list = []

index = 0
list_len = int(input("How many numbers do you want? "))

while index < list_len:
    r = random.randint(0, 101)
    my_list.append(r)
    index += 1

print(my_list)