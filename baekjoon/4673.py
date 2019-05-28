
result_list = [True for _ in range(10001)]
result_list[0] = False

def d(num):
    l = len(str(num))
    
    result = num

    num = str(num)

    for i in range(l):
        
        result += int(num[i])

    return result

for i in range(10001):
    #print(d(i))
    r_num = d(i)
    if r_num <= 10000:
        result_list[d(i)] = False

for i in range(10001):
    if result_list[i]:
        print (i)
