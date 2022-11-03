# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        num_list = []       # num 만 추출
        dash_list = []      # dash count 만 추출
        node_stack = []     # (node, depth)
        
        temp_num = ""
        temp_dash = 0
        
        for x in traversal:
            if x == '-':
                if temp_num != "":
                    num_list.append(int(temp_num))
                temp_dash += 1
                temp_num = ""
            else:
                if temp_dash != 0:
                    dash_list.append(temp_dash)
                temp_num += x
                temp_dash = 0
        num_list.append(int(temp_num))
        
        
        root_node = TreeNode(num_list[0], None, None)
        node_stack = [(root_node, 0)]                   # (Node, depth)
        
        for i in range(1, len(num_list)):
            now_node = TreeNode(num_list[i], None, None)
            now_depth = dash_list[i-1]
            
            # stack top의 depth보다 현재 depth가 더 깊다면, left에 추가
            if node_stack[-1][1] < now_depth:
                node_stack[-1][0].left = now_node
                node_stack.append((now_node, now_depth))
            # 그렇지 않다면 depth가 작아질때까지 올라가서, right에 추가
            else:
                while node_stack and node_stack[-1][1] >= now_depth:
                    node_stack.pop()
                node_stack[-1][0].right = now_node
                node_stack.append((now_node, now_depth))
        
        return root_node
        
        
