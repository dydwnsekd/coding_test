import sys
import operator

n = int(sys.stdin.readline())

for _ in range(n):
    p = int(sys.stdin.readline())
    player_dict = {}

    for _ in range(p):
        value, name = sys.stdin.readline().strip().split()
        player_dict[name] = int(value)

    # sorted_player = sorted(player_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_player = sorted(player_dict.items(), key=operator.itemgetter(1), reverse=True)

    print(sorted_player[0][0])
