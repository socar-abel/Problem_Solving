import sys
sys.setrecursionlimit(10**6)
arr = []
answer = []

while True:
    try:
        x = int(sys.stdin.readline())
        arr.append(x)
    except:
        break


def preorder_to_postorder(tree):
    if len(tree) == 0:
        return
    if len(tree) == 1:
        answer.append(tree[0])
        return

    root = tree[0]
    pivot = len(tree)
    for i in range(1, len(tree)):
        if root < tree[i]:
            pivot = i
            break

    preorder_to_postorder(tree[1:pivot])
    preorder_to_postorder(tree[pivot:])
    answer.append(root)


preorder_to_postorder(arr)
for x in answer:
    print(x)

