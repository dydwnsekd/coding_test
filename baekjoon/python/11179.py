import sys

num = int(sys.stdin.readline())
bin_num = bin(num)
reverse_bin_num = bin_num[2:][::-1]
reverse_num = int(f"0b{reverse_bin_num}", 2)

print(reverse_num)
