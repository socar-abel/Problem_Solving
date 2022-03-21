import sys
N = int(sys.stdin.readline())
tree = dict()
visit1 = dict()
visit2 = dict()
visit3 = dict()

for _ in range(N):
    A, l, r = sys.stdin.readline().split()
    tree[A] = [l, r]
    visit1[A] = False
    visit2[A] = False
    visit3[A] = False


def preorder(node):
    left, right = tree[node]
    visit1[node] = True
    print(node, end='')

    if left != '.' and not visit1[left]:
        preorder(left)

    if right != '.' and not visit1[right]:
        preorder(right)


def inorder(node):
    left, right = tree[node]
    if left != '.' and not visit2[left]:
        inorder(left)

    visit2[node] = True
    print(node, end='')

    if right != '.' and not visit2[right]:
        inorder(right)


def postorder(node):
    left, right = tree[node]
    if left != '.' and not visit3[left]:
        postorder(left)

    if right != '.' and not visit3[right]:
        postorder(right)

    visit3[node] = True
    print(node, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
