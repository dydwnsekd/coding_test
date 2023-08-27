import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    p_list = sys.stdin.readline().strip().split()
    start_p = sys.stdin.readline().strip()
    start_index = p_list.index(start_p)
    n = int(sys.stdin.readline())

    result_index = start_index - n % len(p_list) - 1

    print(p_list[result_index])
