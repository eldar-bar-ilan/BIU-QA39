num: int = int(input("Enter a 3 digit number: "))

if 100 <= num <= 999:
    print(f"the 3 digit is: {num // 100}")
else:
    print(f"Error: {num} is not a 3rd digit number")
