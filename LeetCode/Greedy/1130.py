class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        answer = 0
        temp_arr = arr[:]
        
        while len(temp_arr) >= 2:
            temp_product = [temp_arr[i]*temp_arr[i+1] for i in range(len(temp_arr) - 1)]
            min_product = min(temp_product)
            min_index = temp_product.index(min_product)
            larger_leaf = max(temp_arr[min_index], temp_arr[min_index+1])
            
            temp_arr = temp_arr[:min_index] + [larger_leaf] + temp_arr[min_index+2:]
            answer += min_product
        
        return answer
            
            
