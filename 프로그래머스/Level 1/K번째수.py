def solution(array, commands):
    answer = []
    
    for cmd in commands:
        temp = array[cmd[0]-1:cmd[1]]
        temp.sort()
        answer.append(temp[cmd[2]-1])
    
    return answer
