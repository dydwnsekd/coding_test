import sys

while True:
    x, y = map(int, sys.stdin.readline().split())

    if x == 0 and y == 0:
        break

    bin_x = bin(x)[2:].zfill(8)
    bin_y = bin(y)[2:].zfill(8)

    print(f"{x} = {bin(x)[2:].zfill(8)}")
    print(f"{y} = {bin(y)[2:].zfill(8)}")

    bin2_x = ""
    for i in bin_x:
        if i == "0":
            bin2_x += "1"
        elif i == "1":
            bin2_x += "0"

    bin2_y = ""
    for i in bin_y:
        if i == "0":
            bin2_y += "1"
        elif i == "1":
            bin2_y += "0"

    print(f"-{x} = {bin2_x}")
    print(f"-{y} = {bin2_y}")
