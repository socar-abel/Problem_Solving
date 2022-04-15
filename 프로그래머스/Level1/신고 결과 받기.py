from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_dict = defaultdict(list)
    reported_cnt = defaultdict(int)
    
    for string in report:
        a, b = string.split()
        if b in report_dict[a]:
            continue
        report_dict[a].append(b)
        reported_cnt[b] += 1
    
    for id in id_list:
        tmp = 0
        for x in report_dict[id]:
            if reported_cnt[x] >= k:
                tmp += 1
        answer.append(tmp)
    
    return answer
