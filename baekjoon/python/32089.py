import sys

while True:
    n = int(sys.stdin.readline())
    max_member = 0

    if n == 0:
        break

    members = list(map(int, sys.stdin.readline().strip().split()))

    for i in range(n-2):
        if max_member < sum(members[i:i+3]):
            max_member = sum(members[i:i+3])

    print(max_member)
