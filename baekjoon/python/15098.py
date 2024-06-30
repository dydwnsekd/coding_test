import sys

s_list = sys.stdin.readline().strip().split()

if len(s_list) == len(set(s_list)):
    print("yes")
else:
    print("no")

