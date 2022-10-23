class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        even_sum = 0
        
        for n in nums:
            if n % 2 == 0:
                even_sum += n
        
        
        for add_value, idx in queries:
            
            old_value = nums[idx]
            new_value = old_value + add_value
            
            if new_value % 2 == 0:
                if old_value % 2 == 0:
                    even_sum += add_value
                else:
                    even_sum += new_value
            
            else:
                if old_value % 2 == 0:
                    even_sum -= old_value
            
            nums[idx] = new_value
            answer.append(even_sum)     
                
        
        return answer
