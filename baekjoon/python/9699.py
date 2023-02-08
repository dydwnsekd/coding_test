import sys

cases = int(sys.stdin.readline())

for i in range(cases):
    rice_snak = list(map(int, sys.stdin.readline().split()))

    print(f"Case #{i+1}: {max(rice_snak)}")
