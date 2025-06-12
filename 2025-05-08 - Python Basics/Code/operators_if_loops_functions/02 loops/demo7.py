line = 1
while line <= 3:
    column = 1
    while column <= 3:
        print(f"{line * column}\t", end="")
        column += 1
    print()
    line += 1
