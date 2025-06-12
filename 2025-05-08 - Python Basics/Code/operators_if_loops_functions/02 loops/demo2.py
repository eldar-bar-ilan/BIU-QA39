list_of_names = []
add_more_names = True

while add_more_names:
    name = input("Enter name: ")
    list_of_names.append(name)
    add_more_names = bool(int(input("add more? 1-yes, 0-no: ")))

print(list_of_names)
