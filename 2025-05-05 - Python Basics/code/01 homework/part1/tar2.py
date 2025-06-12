product_name = input("Enter product name: ")
unit_price = float(input("Enter unit price: "))
required_quantity = int(input("Enter required quantity: "))

total_due = unit_price * required_quantity

# use f-string for easy messages
msg = f"You want {required_quantity} units of {product_name}. total due is {total_due}"

print(msg)





