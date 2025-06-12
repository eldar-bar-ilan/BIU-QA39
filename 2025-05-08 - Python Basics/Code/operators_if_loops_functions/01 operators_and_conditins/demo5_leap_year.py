year = int(input("Enter a Year: "))
# year = 600
# False or (True and False) = False or False = False
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
