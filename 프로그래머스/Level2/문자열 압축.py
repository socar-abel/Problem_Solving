def solution(s):
    compressed = []
    
    if len(s) == 1 : return 1
    
    for unit in range(len(s)//2):
        #print('unit:',unit+1)
        splited = []
        i = 0
        
        # unit 단위로 문자열 자르기
        while i < len(s):
            splited.append(s[i:i+unit+1])
            i = i + unit + 1
        #print('before:',splited)
        
        # 예외처리
        # if splited[0] != splited[1] : continue 
            
        # 자른 문자열이 몇번 반복되는지
        count = 1
        j = 0
            
        while j <= len(splited)-2:
            # print('내부:',splited)
            
            if splited[j] == splited[j+1] :
                count += 1
                del splited[j+1]
                splited[j] = str(count)+splited[j]
            
            elif splited[j][0].isdigit():
                k = 0
                while splited[j][k].isdigit():
                    k += 1
                
                if splited[j][k:] == splited[j+1]:
                    count+=1
                    del splited[j+1]
                    splited[j] = str(count)+splited[j][k:]
                else:
                    count = 1
                    j += 1
            else :
                count = 1
                j += 1
    
        #print('after:',splited)
        compressed.append("".join(splited))
                    
    #print('compressed:',compressed)        
    
    
    return len(s) if not compressed else len(min(compressed, key = lambda x : len(x)))
