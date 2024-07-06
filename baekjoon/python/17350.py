import sys

n = int(sys.stdin.readline())
player_list = []

for _ in range(n):
    player_list.append(sys.stdin.readline().strip())

if "anj" in player_list:
    print("뭐야;")
else:
    print("뭐야?")

