from collections import defaultdict
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        
    for key in graph:
        graph[key].sort()
        
    def dfs(node, path):
        if len(path) == len(tickets) + 1:
            return path
    
        for i, city in enumerate(graph[node]):
            graph[node].pop(i)
            
            newPath = path[:]
            newPath.append(city)
            
            result = dfs(city, newPath)
            if result: return result
            
            graph[node].insert(i,city)
    
    answer = dfs("ICN",["ICN"])
    
    return answer

