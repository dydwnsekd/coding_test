import sys

def reverse_bit(binary_num):
    binary_result = ""
    for i in binary_num:
        if i == "0":
            binary_result += "1"
        else:
            binary_result += "0"

    return binary_result


a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

bin_len = len(a)
a = int(a, 2)
b = int(b, 2)

print(format(a & b, f'0{bin_len}b'))
print(format(a | b, f'0{bin_len}b'))
print(format(a ^ b, f'0{bin_len}b'))
print(reverse_bit(format(a, f'0{bin_len}b')))
print(reverse_bit(format(b, f'0{bin_len}b')))
