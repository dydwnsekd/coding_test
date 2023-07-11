import sys

def twos_complement(decimal_number, length):
    bin_number = bin(decimal_number)[2:].zfill(length)
    temp_number = ''.join('1' if b == '0' else '0' for b in bin_number)
    return_number = bin(int("0b" + temp_number, 2) + 1)[2:].zfill(length)

    return return_number

while True:
    x, y = map(int, sys.stdin.readline().split())

    if x == 0 and y == 0:
        break

    bin_x = bin(x)[2:].zfill(8)
    bin_y = bin(y)[2:].zfill(8)

    print(f"{x} = {bin(x)[2:].zfill(8)}")
    print(f"{y} = {bin(y)[2:].zfill(8)}")
    print(f"-{x} = {twos_complement(x, 8)}")
    print(f"-{y} = {twos_complement(y, 8)}")
    if x >= y:
        print(f"{x-y} = {bin(x-y)[2:].zfill(8)}")
    else:
        print(f"{x-y} = {twos_complement(y-x, 8)}")

    print()

