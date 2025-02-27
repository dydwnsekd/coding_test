import sys

find_s = ["M", "O", "B", "I", "S"]
s = sys.stdin.readline().strip()

if all([i in s for i in find_s]):
    print("YES")
else:
    print("NO")
