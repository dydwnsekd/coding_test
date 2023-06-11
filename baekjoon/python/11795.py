import sys

days = int(sys.stdin.readline())
sets = [0, 0, 0]

for _ in range(days):
    temp_sets = list(map(int, sys.stdin.readline().split()))
    sets[0] += temp_sets[0]
    sets[1] += temp_sets[1]
    sets[2] += temp_sets[2]

    if min(sets) < 30:
        print("NO")
    else:
        deploy_sets = min(sets)
        print(deploy_sets)
        sets[0] -= deploy_sets
        sets[1] -= deploy_sets
        sets[2] -= deploy_sets
