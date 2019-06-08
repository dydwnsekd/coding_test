import sys

end_zero = [0 for _ in range(92)]
end_one = [0 for _ in range(92)]
result_list = [0 for _ in range(92)]

end_one[1] = 1
end_zero[2] = 1

result_list[1] = 1
result_list[2] = 1

for i in range(3, 92):
    end_zero[i] = end_zero[i-1] + end_one[i-1]
    end_one[i] = end_zero[i-1]
    result_list[i] = end_zero[i] + end_one[i]

num = int(sys.stdin.readline())

print (result_list[num])

