import sys

case_count = int(sys.stdin.readline())

for _ in range(case_count):
    num = sys.stdin.readline().split(" ")

    a = int(num[0])
    b = int(num[1])

    print (a+b)
