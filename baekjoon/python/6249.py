import sys

n, p, h = list(map(int, sys.stdin.readline().split()))

for _ in range(n):
    value = int(sys.stdin.readline())

    if value < p:
        print(f"NTV: Dollar dropped by {p-value} Oshloobs")
    if value > h:
        print(f"BBTV: Dollar reached {value} Oshloobs, A record!")
        h = value

    p = value

