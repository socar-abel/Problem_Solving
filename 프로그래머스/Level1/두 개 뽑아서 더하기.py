from itertools import combinations

def solution(numbers):
    answer = []
    
    combi = list(combinations(numbers,2))
    for c in combi:
        answer.append(sum(c))
    
    answer = list(set(answer))
    answer.sort()
    
    return answer
  
  
  # set을 사용하면 순서가 뒤죽박죽 된다는 것을 잊지말아야 한다.
