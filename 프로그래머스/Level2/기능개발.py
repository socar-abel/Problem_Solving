def solution(progresses, speeds):
    answer = []
    complete = [False*len(progresses)]
    require = []
    
    for i in range(len(progresses)):
        time = (100-progresses[i]) / speeds[i]
        if time % 1 == 0: require.append(int(time))
        else : require.append(int(time)+1)
    
    print(require)
    i = 0
    while i < len(require):
        day = require[i]
        count = 1
        i += 1
        while i < len(require) and require[i] <= day :
            i += 1
            count += 1
        
        answer.append(count)
        
    return answer
