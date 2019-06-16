import sys

problem_count = int(sys.stdin.readline())
count = 0

for _ in range(problem_count):
    check_flag = True
    alpa_list = list()

    input_str = sys.stdin.readline()
    before_alpa = input_str[0]

    for i in input_str[1:]:
        if i == before_alpa:
            continue
        elif i in alpa_list:
            check_flag = False
            break
        else:
            alpa_list.append(before_alpa)
            before_alpa = i

    if check_flag:
        count += 1

print (count)