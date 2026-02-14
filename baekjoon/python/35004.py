import sys

count = 0

n = int(sys.stdin.readline())
bin_n = bin(n)

while int(bin_n, 2) != 0:
    reverse_n = '0b' + bin_n[2:][::-1]
    bin_n = bin(int(reverse_n, 2) - 1)

    count += 1

print(count)

