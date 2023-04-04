import sys

cases = int(sys.stdin.readline())
a_count = 0
b_count = 0

for i in sys.stdin.readline().strip():
    if i == "A":
        a_count += 1
    else:
        b_count += 1

if a_count == b_count:
    print("Tie")
elif a_count > b_count:
    print("A")
else:
    print("B")
