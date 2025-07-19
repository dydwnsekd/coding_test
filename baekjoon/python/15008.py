import sys

bob, alice = 0, 0

n = int(sys.stdin.readline())
a_list = list(map(int, sys.stdin.readline().strip().split()))
a_list.sort(reverse=True)

for i in range(len(a_list)):
    if i % 2 == 0:
        bob += a_list[i]
    else:
        alice += a_list[i]

print(bob, alice)


