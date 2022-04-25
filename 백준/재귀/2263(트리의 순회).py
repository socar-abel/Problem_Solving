import sys
sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline())

inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
answer = []


def recursion(in_idx, post_idx):
    # print('inorder idx',in_idx)
    # print('postorder idx',post_idx)
    if in_idx[0] > in_idx[1]:
        return

    if in_idx[0] == in_idx[1]:
        answer.append(in_idx[0])
        return

    mid_value = postorder[post_idx[1]]
    in_mid_idx = 0

    for i in range(in_idx[0], in_idx[1]+1):
        if inorder[i] == mid_value:
            in_mid_idx = i
            break

    left_tree_cnt = in_mid_idx - in_idx[0]
    # print('left tree cnt', left_tree_cnt)
    # print()
    left_inorder = (in_idx[0], in_mid_idx - 1)
    left_postorder = (post_idx[0], post_idx[0] + left_tree_cnt - 1)

    if in_mid_idx == in_idx[1]:
        answer.append(in_mid_idx)
        recursion(left_inorder, left_postorder)
        return

    right_inorder = (in_mid_idx + 1, in_idx[1])
    right_postorder = (post_idx[0] + left_tree_cnt, post_idx[1] - 1)

    answer.append(in_mid_idx)
    recursion(left_inorder, left_postorder)
    recursion(right_inorder, right_postorder)
    return


recursion((0, n-1), (0, n-1))

for a in answer:
    print(inorder[a], end=' ')
