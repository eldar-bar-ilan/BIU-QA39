from my_modules.general import get_random_list

ls = get_random_list()
print(ls)
# print the sum of numbers in the list
index = 0
sum_ = 0
while index < len(ls):
    current = ls[index]
    sum_ += current
    index += 1
print(f"sum is: {sum_}")

