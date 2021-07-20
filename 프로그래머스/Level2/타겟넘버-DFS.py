# 이 풀이가 더 정석적이고, 알고리즘적으로 좋은 풀이인듯하다.

answer = 0
def DFS(index,numbers,target,value):
    global answer
    if index == len(numbers) and target == value : 
        answer += 1
        return
    elif index == len(numbers) : return
    
    DFS(index+1,numbers,target,value+numbers[index])
    DFS(index+1,numbers,target,value-numbers[index])
        

def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer
