class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        answer = 0
        N = len(grades)
        
        temp_group_num = 1
        
        while True:
            if N < temp_group_num:
                break
            
            N -= temp_group_num
            temp_group_num += 1
            answer += 1
        
        print(answer)
        return answer
        
