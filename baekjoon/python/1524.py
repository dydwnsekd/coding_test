import sys

t = int(sys.stdin.readline())

for _ in range(t):
    sys.stdin.readline()

    sj, sb = map(int, sys.stdin.readline().strip().split())

    sj_list = sorted(list(map(int, sys.stdin.readline().strip().split())))
    sb_list = sorted(list(map(int, sys.stdin.readline().strip().split())))

    while len(sj_list) > 0 and len(sb_list) > 0:
        if sj_list[0] >= sb_list[0]:
            sb_list.remove(sb_list[0])
        elif sj_list[0] < sb_list[0]:
            sj_list.remove(sj_list[0])

    if sj_list:
        print("S")
    else:
        print("B")

