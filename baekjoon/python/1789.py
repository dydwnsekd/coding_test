import sys

hap = 0
count = 1

S = int(sys.stdin.readline())

while True:
    hap += count
    if hap > S:
        break
    count += 1

print (count-1)