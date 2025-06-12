password = "eldar2004"
user_input = input("Enter password: ")
counter: int = 1

while counter < 3 and user_input != password:
    user_input = input("Wrong password. Enter password again: ")
    counter = counter + 1

if user_input == password:
    print("You are logged in")
else:
    print("Login failed")
