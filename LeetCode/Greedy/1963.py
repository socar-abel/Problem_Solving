class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for x in s:
            if stack:
                if stack[-1] == "[":
                    if x == "]":
                        stack.pop()
                    else:
                        stack.append(x)
                elif stack[-1] == "]":
                    stack.append(x)
            else:
                stack.append(x)
        
        pair = len(stack) // 2
        
        return (pair+1) // 2
        
            
