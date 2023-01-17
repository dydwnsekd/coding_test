import sys

n = int(sys.stdin.readline())

for i in range(n):
    first_name = sys.stdin.readline().strip()
    last_name = sys.stdin.readline().strip()
    print(f"Case {i+1}: {last_name}, {first_name}")
