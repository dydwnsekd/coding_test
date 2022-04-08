from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(list)
    count = 0
    temp_count = 1
    for clothe in clothes:
        k = clothe[1]
        v = clothe[0]
        clothes_dict[k].append(v)

    for k in clothes_dict.keys():
        count += len(clothes_dict[k])
        temp_count *= len(clothes_dict[k])
    
    if len(clothes_dict.keys()) != 1:
        count += temp_count
    return count