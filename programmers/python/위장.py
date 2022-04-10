from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(list)
    count = 1

    for clothe in clothes:
        k = clothe[1]
        v = clothe[0]
        clothes_dict[k].append(v)

    for k in clothes_dict.keys():
        count *= len(clothes_dict[k]) + 1
        
    return count-1