from my_modules.general import get_random_list

ls = get_random_list()
print(ls)
# print the sum of numbers in the list
sum_ = 0
for current in ls:
    sum_ += current
print(f"sum is: {sum_}")

