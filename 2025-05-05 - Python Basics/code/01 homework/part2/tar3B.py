import random

r = random.randrange(0, 101)
print(r)

msg = f"Thanks. The number {r} is "

if r % 2 == 0:
    msg = msg + "even"
else:
    msg = msg + "odd"

print(msg)



