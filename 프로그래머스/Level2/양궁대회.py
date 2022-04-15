from itertools import combinations
from collections import defaultdict

def solution(n, info):
    answer = [-1]
    point = [x for x in range(11)]
    score_gap = defaultdict(list)
    appeach_score = 0
    
    for i in range(11):
        if info[i] > 0:
            appeach_score += (10 - i)
    
    # 11 가지 중 몇가지의 점수를 먹을건지. combis[2] = 11C2
    combis = []
    for i in range(1, n+1):
        combis += list(combinations(point, i)) 
    
    
    for combi in combis:
        temp_appeach_score = appeach_score
        candidate = [0 for _ in range(11)]
        can = True
        arrow = n
        lion_score = 0
        
        for score in combi:
            need = info[10 - score] + 1
            candidate[10 - score] += need
            if arrow - need < 0:
                can = False
                break
            arrow -= need
            lion_score += score
            if need >= 2:
                temp_appeach_score -= score
            
        if can:
            candidate[-1] += arrow
            score_gap[lion_score - temp_appeach_score].append(candidate)
    
    key = list(score_gap.keys())
    key.sort()
    
    
    if key[-1] > 0:
        results = score_gap[key[-1]]
        for i in range(11):
            max_index = -1
            max_cnt = 0
            for j in range(len(results)):
                if results[j][10 - i] > 0:
                    if max_cnt < results[j][10 - i]:
                        max_index = j
            if max_index != -1:
                answer = results[max_index]
                break
        
    return answer
