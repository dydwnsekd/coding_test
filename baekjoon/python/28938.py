import sys

n = int(sys.stdin.readline())
sequence_list = list(map(int, sys.stdin.readline().split()))

if sequence_list.count(1) == sequence_list.count(-1):
    print("Stay")
elif sequence_list.count(1) > sequence_list.count(-1):
    print("Right")
else:
    print("Left")

