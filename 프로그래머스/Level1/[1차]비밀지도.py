def solution(n, arr1, arr2):
    answer = []
    
    map1 = []
    map2 = []
    
    for i in range(n):
        temp1 = format(arr1[i],'b')        
        temp2 = format(arr2[i],'b')   
        
        if len(temp1) < n:
            while not len(temp1) == n:
                temp1 = '0' + temp1
        if len(temp2) < n:
            while not len(temp2) == n:
                temp2 = '0' + temp2
    
        map1.append(temp1)
        map2.append(temp2)
    
    for i in range(n):
        sumMap = ''
        for j in range(n):
            if map1[i][j] == '0' and map2[i][j] == '0' :
                sumMap += ' '
            else :
                sumMap += '#'
        answer.append(sumMap)
    
    return answer
