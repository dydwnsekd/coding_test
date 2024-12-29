import sys

n = int(sys.stdin.readline())

def sequence(num):
    if num == 1:
        return n
    elif num % 2 == 1:
        return sequence(sequence(num-1)//2)
    elif num % 2 == 0:
        return 3 * sequence(num-1) + 1

count = 1

sequence_list = [n]
print(sequence(2))

while True:
    count += 1

    sequence_list.append(sequence(count))

    if sequence_list[count-1] == 1:
        print(count)
        break



