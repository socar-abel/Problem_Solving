def weakDFS(num, weak, ranking):
    if ranking[num]['before']:
        for x in ranking[num]['before']:
            if not x in weak: 
                weak.append(x)
                weakDFS(x,weak,ranking)

def strongDFS(num, strong, ranking):
    if ranking[num]['after']:
        for x in ranking[num]['after']:
            if not x in strong: 
                strong.append(x)
                strongDFS(x,strong,ranking)    
        
def solution(n, results):
    answer = 0
    ranking = []
    for x in range(n+1):
        tempDict = {'number':x,'before':[], 'after':[]}
        ranking.append(tempDict)
    
    for i in range(len(results)):
        winner = results[i][0]
        loser = results[i][1]
        ranking[loser]['after'].append(winner)
        ranking[winner]['before'].append(loser)    
    
    for rank in ranking:
        weak = []; strong = []
        
        for weaker in rank['before']:
            weak.append(weaker)
        for stronger in rank['after']:
            strong.append(stronger)
            
        for w in weak:
            weakDFS(w, weak, ranking)
        for s in strong:
            strongDFS(s, strong, ranking)
    
        if len(weak) + len(strong) == n-1 : answer += 1

    return answer
