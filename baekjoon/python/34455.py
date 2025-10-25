import sys

q = int(sys.stdin.readline())
event_count = int(sys.stdin.readline())

for event in range(event_count):
    operator = sys.stdin.readline().strip()
    c = int(sys.stdin.readline())

    if operator == '+':
        q += c
    elif operator == '-':
        q -= c

print(q)
