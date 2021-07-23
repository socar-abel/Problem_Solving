def solution(record):
    answer = []
    ID_Name = {}
    result = []
    
    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            result.append(r[1]+' 님이 들어왔습니다.')
            ID_Name[r[1]] = r[2]
            
        elif r[0] == 'Leave':
            result.append(r[1]+' 님이 나갔습니다.')
            
        elif r[0] == 'Change' :
            ID_Name[r[1]] = r[2]
    
    
    for i in range(len(result)):
        result[i] = result[i].replace(result[i].split()[0],ID_Name[result[i].split()[0]])
        result[i] = result[i].split()[0] + result[i].split()[1] + ' '  +result[i].split()[2]
        
    
    return result
