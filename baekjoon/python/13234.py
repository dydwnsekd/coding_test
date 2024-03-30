import sys

a, o, b = sys.stdin.readline().strip().split()

if o == "AND":
    if a == "false" or b == "false":
        print("false")
    else:
        print("true")

elif o == "OR":
    if a == "true" or b == "true":
        print("true")
    else:
        print("false")
