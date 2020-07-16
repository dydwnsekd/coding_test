import sys

glass_count = int(sys.stdin.readline())

wine_value = list()
result_list = [[0] * 3 for i in range(glass_count)]

for _ in range(glass_count):
    wine_value.append(int(sys.stdin.readline()))

# [i][0] 이전의 2잔은 연속해서 먹은 경우(i-1, i-2) => i잔 먹지 x
# [i][1] 이전의 잔을 1잔만 먹은 경우(i-1)          => i잔 먹음
# [i][2] 이전의 잔을 먹지 않은 경우                => i잔 먹음

result_list[0][1] = wine_value[0]
result_list[0][2] = wine_value[0]

if glass_count >= 2:
    
    result_list[1][0] = wine_value[0]
    result_list[1][1] = wine_value[0] + wine_value[1]
    result_list[1][2] = wine_value[1]

    for i in range(2, glass_count):
        result_list[i][0] = max(result_list[i-1])
        result_list[i][1] = max(max(result_list[i-2]), result_list[i-1][2]) + wine_value[i]
        result_list[i][2] = max(result_list[i-2]) + wine_value[i]

print (max(result_list[glass_count-1]))

