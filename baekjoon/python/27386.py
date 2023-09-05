import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

combine_text = a+b

print("".join(sorted(combine_text)))
