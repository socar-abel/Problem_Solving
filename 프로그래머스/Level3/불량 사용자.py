from collections import defaultdict
from itertools import product   

def check(user,ban):
    answer = True; N = len(ban)
    if len(user) != N : return False
    for i in range(N):
        if ban[i] == '*': continue
        else:
            if user[i] != ban[i]: answer = False; break
    return answer

def solution(user_id, banned_id):
    candidate = defaultdict(list)
    
    for i in range(len(banned_id)):
        for user in user_id:
            if check(user,banned_id[i]): candidate[i].append(user)

    # 여기부터 수정
    candy = candidate.values()
    #print(candy)
    cartesian = list(product(*candy))

    answer = set()
    for cart in cartesian:
        if len(set(cart)) == len(banned_id):
            #print(sorted(set(cart)))
            answer.add("".join(sorted(set(cart))))
    
    return len(answer)
