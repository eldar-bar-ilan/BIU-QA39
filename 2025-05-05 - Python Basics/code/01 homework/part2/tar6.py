num: int = int(input("Enter a number: "))
print(f"The second digit from right of {num} is {num // 10 % 10}")
print(f"The third digit from right of {num} is {num // 100 % 10}")
print(f"The forth digit from right of {num} is {num // 1000 % 10}")
