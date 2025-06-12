grade: int = int(input("Enter grade 0 - 10: "))

if 0 <= grade <= 6:
    print("Fail")
elif 7 <= grade <= 8:
    print("Good")
elif 9 <= grade <= 10:
    print("Great")
else:
    print(f"Error: {grade} is out of range!")

