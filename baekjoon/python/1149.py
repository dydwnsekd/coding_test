import sys

house = int(sys.stdin.readline())
RGB_list = []

result_list = [[0]*3 for _ in range(house)]

#[0] R
#[1] G
#[2] B

for _ in range(house):
    RGB_list.append(list(map(int, sys.stdin.readline().split(" "))))

result_list[0][0] = RGB_list[0][0]
result_list[0][1] = RGB_list[0][1]
result_list[0][2] = RGB_list[0][2]

for i in range(1, house):
    result_list[i][0] = min(result_list[i-1][1], result_list[i-1][2]) + RGB_list[i][0]
    result_list[i][1] = min(result_list[i-1][0], result_list[i-1][2]) + RGB_list[i][1]
    result_list[i][2] = min(result_list[i-1][0], result_list[i-1][1]) + RGB_list[i][2]

print (min(result_list[house-1]))