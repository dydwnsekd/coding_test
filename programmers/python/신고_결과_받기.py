from collections import defaultdict

def solution(id_list, reports, k):
    answer = []
    report_dict = defaultdict(list)
    report_count = []
    
    for report in reports:
        k, v = report.split()
        report_dict[k].append(v)
        
    for k, v in report_dict.items():
        report_count.extend(list(set(v)))
        
    for id in id_list:
        answer.append(report_count.count(id))
        
    print(report_count)
    print(answer)
        
    return answer