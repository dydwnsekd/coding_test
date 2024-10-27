import sys

n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().strip()
    result = ""

    for j in s:
        if ord(j) + 1 > ord("Z"):
            result += "A"
        else:
            result += chr(ord(j) + 1)

    print(f"String #{i + 1}")
    print(result)
    print()
