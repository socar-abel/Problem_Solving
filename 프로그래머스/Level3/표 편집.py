def solution(n, k, cmds):
    answer = ['O'] * n
    # Double Linked List
    DLL = {i : [i-1,i+1] for i in range(n)}
    DLL[0][0] = 'HEAD'; DLL[n-1][1] = 'TAIL'
    stack = []
    
    for cmd in cmds:
        #print('현재 k',k)
        if cmd[0] == 'D':
            x = int(cmd[2:])
            for _ in range(x):
                k = DLL[k][1]
                
        elif cmd[0] == 'U':
            x = int(cmd[2:])
            for _ in range(x):
                k = DLL[k][0]
        
        elif cmd[0] == 'C':
            prev, next = DLL[k]
            answer[k] = 'X'

            if prev == 'HEAD':
                stack.append([k,prev,next])
                DLL[next][0] = 'HEAD'
                k = next
            
            elif next == 'TAIL':
                stack.append([k,prev,next]) # 삭제
                DLL[prev][1] = 'TAIL'
                k = prev    # 윗 행 선택
            
            else:
                stack.append([k,prev,next]) # 삭제
                DLL[prev][1] = next
                DLL[next][0] = prev
                k = next   # 아래 행 선택
                
        elif cmd[0] == 'Z':
            now, prev, next = stack.pop()
            answer[now] = 'O'
            
            if prev == 'HEAD':
                DLL[next][0] = now
            elif next == 'TAIL':
                DLL[prev][1] = now
            else:
                DLL[prev][1] = now
                DLL[next][0] = now          
    
    #print('stack[0]', list(map(lambda x : x[0], stack)))
    
    return ''.join(answer)


