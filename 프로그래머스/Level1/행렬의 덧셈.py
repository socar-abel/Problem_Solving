def solution(arr1, arr2):
    answer = []
    for a in range(len(arr1)):
        temp = []
        for b in range(len(arr1[a])):
            temp.append(arr1[a][b]+arr2[a][b])
        answer.append(temp)
    return answer
