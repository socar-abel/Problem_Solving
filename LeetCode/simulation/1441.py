from collections import deque

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = []
        stream = list(range(1, n+1))
        stack = deque()
        queue = deque(target[:])
        
        for x in stream:
            stack.append(x)
            answer.append("Push")
            
            if stack and queue and stack[-1] != queue[0]:
                stack.pop()
                answer.append("Pop")
            else:
                if queue:
                    queue.popleft()
  
            if stack == deque(target):
                break
        
        return answer
