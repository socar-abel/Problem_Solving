'''
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
'''

class Solution:

    def __init__(self):
        self.answer = []
    
    def dfs(self, node: 'Optional[Node]'):
        if node == None:
            return
        
        self.answer.append(node)
        
        # 자식이 있다면 자식부터 탐색
        if node.child != None:
            self.dfs(node.child)
        
        # 다음 노드가 있다면 탐색
        if node.next != None:
            self.dfs(node.next)
    
    
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.dfs(head)

        new_head = None
        if len(self.answer) >= 1:
            new_head = self.answer[0]
            new_head.child = None
        temp_node = new_head
        
        for node in self.answer[1:]:
            new_node = node
            new_node.child = None
            temp_node.next = new_node
            new_node.prev = temp_node
            temp_node = new_node
        
        return new_head
