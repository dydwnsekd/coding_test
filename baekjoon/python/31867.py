import sys

n = int(sys.stdin.readline())
k = sys.stdin.readline().strip()

odd_count = 0
even_count = 0

for i in k:
    if int(i) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count > odd_count:
    print("0")
elif odd_count > even_count:
    print("1")
else:
    print("-1")
