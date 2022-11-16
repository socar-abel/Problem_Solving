import sys

def find_parent(x, parent):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    px = find_parent(x, parent)
    py = find_parent(y, parent)
    parent[max(px, py)] = min(px, py)

t = 1
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    p = [x for x in range(n+1)]
    edges = [[] for _ in range(n+1)]
    parent_set = set()
    cycle_child = []

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        edges[a].append(b)

    for i in range(1, n+1):
        pi = find_parent(i, p)
        for j in edges[i]:
            pj = find_parent(j, p)
            if pi == pj:
                cycle_child.append(i)
                cycle_child.append(j)
            else:
                union(i, j, p)


    for i in range(1, n+1):
        parent_set.add(find_parent(i, p))

    cycle_parent = set()
    for c in cycle_child:
        cycle_parent.add(find_parent(c, p))

    tree_cnt = len(parent_set) - len(cycle_parent)
    answer = ''
    if tree_cnt == 0:
        answer = 'Case {0}: No trees.'.format(t)
    elif tree_cnt == 1:
        answer = 'Case {0}: There is one tree.'.format(t)
    else:
        answer = 'Case {0}: A forest of {1} trees.'.format(t, tree_cnt)
    print(answer)

    t += 1


