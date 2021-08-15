def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    
    col = [[] for _ in range(len(arr2[0]))]
    for b in range(len(arr2[0])):
        for a in range(len(arr2)):
            col[b].append(arr2[a][b])
    
    size = len(arr1[0])
    
    for i in range(len(arr1)):
        for j in range(len(col)):
            tempResult = 0
            for x in range(size):
                tempResult += arr1[i][x] * col[j][x]
            answer[i].append(tempResult)
        
    return answer
