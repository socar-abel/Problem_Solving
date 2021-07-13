def solution(lottos, win_nums):
    answer = [-1,-1]
    count = 0
    
    for lotto in lottos:        
        if not lotto == 0 and lotto in win_nums:
            count += 1       
            
    zero = lottos.count(0)
    max = count + zero
    min = count
    
    dict = {6:'1',5:'2',4:'3',3:'4',2:'5'}
    answer[0] = int(dict[max]) if max in dict else 6
    answer[1] = int(dict[min]) if min in dict else 6
    
    return answer
