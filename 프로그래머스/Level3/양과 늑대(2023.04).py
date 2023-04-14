import sys
import copy
from collections import defaultdict
sys.setrecursionlimit(10**6)
answer = 0
tree = defaultdict(list)


def dfs(info, edges, node, sheep, wolves, next_nodes):
    global answer, tree
    if info[node] == 0: 
        sheep += 1
        answer = max(answer, sheep)
    else: 
        wolves += 1
    new_next_nodes = next_nodes + tree[node]
    
    for next_node in new_next_nodes:
        x = copy.deepcopy(new_next_nodes)
        x.remove(next_node)
        if info[next_node] == 0:    
            dfs(info, edges, next_node, sheep, wolves, x)
        else:
            if sheep <= wolves + 1:
                continue
            else:
                dfs(info, edges, next_node, sheep, wolves, x)

                
def solution(info, edges):   
    global tree
    for parent, child in edges:
        tree[parent].append(child)

    dfs(info, edges, 0, 0, 0, [])
    return answer
