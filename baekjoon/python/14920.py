# import sys
#
# n = int(sys.stdin.readline())
#
# sequence_list = [n]
#
# def sequence(num):
#     if num == 1:
#         return sequence_list[0]
#     elif sequence_list[num-2] % 2 == 0:
#         return sequence_list[num-2] // 2
#     elif sequence_list[num-2] % 2 == 1:
#         return 3 * sequence_list[num-2] + 1
#
# count = 1
#
# while True:
#     count += 1
#
#     sequence_list.append(sequence(count))
#
#     if n == 1:
#         print(1)
#         break
#
#     if sequence_list[count-1] == 1:
#         print(count)
#         break
#

import sys

n = int(sys.stdin.readline().strip())

sequence_list = [n]

def generate_sequence(num):
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        sequence_list.append(num)

generate_sequence(n)

print(len(sequence_list))
