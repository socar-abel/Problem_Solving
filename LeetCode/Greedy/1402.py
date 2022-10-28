class Solution:
    
    def get_coefficient(self, satisfaction, idx):
        result = 0
        time = 1
        for i in range(idx, len(satisfaction)):
            result += time * satisfaction[i]
            time += 1
        return result
    
    
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        answer = 0
        N = len(satisfaction)
        satisfaction.sort()
        
        for i in range(N):
            temp = self.get_coefficient(satisfaction, i)
            answer = max(answer, temp)
        return answer
            
