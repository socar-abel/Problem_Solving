from collections import deque

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped = deque(popped)
        stack = deque()
        
        for x in pushed:
            stack.append(x)
            
            while stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped.popleft()

        while stack:
            if stack[-1] == popped[0]:
                stack.pop()
                popped.popleft()
            else:
                break
        
        return False if stack else True
        
            
        
        
                
        
