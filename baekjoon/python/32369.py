import sys

n, a, b = map(int, sys.stdin.readline().strip().split())
onion_a = onion_b = 1

for _ in range(n):
    onion_a += a
    onion_b += b

    if onion_a < onion_b:
        onion_a, onion_b = onion_b, onion_a
    elif onion_a == onion_b:
        onion_b -= 1

print(onion_a, onion_b)

