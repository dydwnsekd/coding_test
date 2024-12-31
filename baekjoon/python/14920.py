import sys

n = int(sys.stdin.readline())

sequence_list = [n]

def sequence(num):
    if num == 1:
        return sequence_list[0]
    elif sequence_list[num-2] % 2 == 0:
        return sequence_list[num-2] // 2
    elif sequence_list[num-2] % 2 == 1:
        return 3 * sequence_list[num-2] + 1

count = 1

while True:
    count += 1
    sequence_list.append(sequence(count))

    if sequence_list[count-1] == 1:
        print(count)
        break
