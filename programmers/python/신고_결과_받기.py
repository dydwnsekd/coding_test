from collections import defaultdict

def solution(id_list, reports, k):
    answer = [0] * len(id_list)
    plaintiff_dict = defaultdict(list)
    defendant_dict = defaultdict(int)
    
    for report in reports:
        key, value = report.split()
        plaintiff_dict[key].append(value)
        defendant_dict[value] = defendant_dict[value] + 1
    
    for id_index in range(len(id_list)):
        id = id_list[id_index]
        if id in plaintiff_dict:
            for i in plaintiff_dict[id]:
                if defendant_dict[i] >= int(k):
                    answer[id_index] = answer[id_index] + 1
                    
    print(plaintiff_dict)
    print(defendant_dict)
    
    return answer