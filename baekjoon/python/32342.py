import sys

q = int(sys.stdin.readline())

for _ in range(q):
    result = 0
    s = sys.stdin.readline().strip()

    for i in range(len(s) - 2):
        if s[i:i+3] == "WOW":
            result += 1

    print(result)

