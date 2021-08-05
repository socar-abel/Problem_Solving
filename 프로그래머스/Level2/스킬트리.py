def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        temp = []
        for t in tree:
            if t in skill: temp.append(t)
        if "".join(temp) == skill[:len(temp)] : answer += 1
                
    return answer
