import sys

n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().strip()
    if command.startswith('Simon says '):
        print(command.replace('Simon says', ''))
