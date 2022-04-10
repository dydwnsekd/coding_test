def solution(id_list, reports, k):
    answer = [0] * len(id_list)
    defendant_dict = {x : 0 for x in id_list}
    
    for report in set(reports):
        defendant_dict[report.split()[1]] += 1
    
    for report in set(reports):
        if defendant_dict[report.split()[1]] >= k:
            answer[id_list.index(report.split()[0])] += 1
    
    return answer

