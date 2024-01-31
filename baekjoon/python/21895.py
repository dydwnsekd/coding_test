import sys

result = ""
cases = int(sys.stdin.readline())

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

for i in range(cases):
    t1 = a[i]
    t2 = b[i]

    if t1 == "R":
        if t2 == "R":
            result += "P"
        elif t2 == "P":
            result += "P"
        elif t2 == "S":
            result += "R"

    if t1 == "P":
        if t2 == "R":
            result += "P"
        elif t2 == "P":
            result += "S"
        elif t2 == "S":
            result += "S"

    if t1 == "S":
        if t2 == "R":
            result += "R"
        elif t2 == "P":
            result += "S"
        elif t2 == "S":
            result += "R"

print(result)
