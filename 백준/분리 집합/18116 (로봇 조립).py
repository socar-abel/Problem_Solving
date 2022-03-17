import sys
N = int(sys.stdin.readline())
cmd = []

for _ in range(N):
    cmd.append(sys.stdin.readline().split())

parent = [x for x in range(10**6 + 1)]
set_size = [1 for x in range(10**6 + 1)]


def find_root(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_root(parent[x])
        return parent[x]


def union(a, b):
    pa = find_root(a)
    pb = find_root(b)

    if pa < pb:
        parent[pb] = pa
        set_size[pa] += set_size[pb]
        set_size[pb] = 0
    elif pb < pa:
        parent[pa] = pb
        set_size[pb] += set_size[pa]
        set_size[pa] = 0
    # 서로 이미 루트 노드가 같다면
    else:
        pass


for query in cmd:
    # 합집합
    if query[0] == 'I':
       union(int(query[1]), int(query[2]))
    # 질문
    elif query[0] == 'Q':
        c = int(query[1])
        pc = find_root(c)
        print(set_size[pc])

