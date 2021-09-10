def solution(n, k, cmds):
    answer = ['O'] * n
    table = {x:[x-1,x+1] for x in range(n)}
    table[0][0] = 'head'; table[n-1][1] = 'tail'
    
    now = k; stack = []
    
    for cmd in cmds:
        if cmd[0] == 'U':
            X = int(cmd[2:])
            for _ in range(X): now = table[now][0]
                
        elif cmd[0] == 'D':
            X = int(cmd[2:])
            for _ in range(X): now = table[now][1]
                
        elif cmd[0] == 'C':
            before = table[now][0]
            after = table[now][1]
            answer[now] = 'X'
            stack.append((now,before,after))
            
            if before == 'head':
                table[after][0] = 'head'
                now = after
            
            elif after == 'tail':
                table[before][1] = 'tail'
                now = before
                
            else:
                table[before][1] = after
                table[after][0] = before
                now = after
            
        elif cmd[0] == 'Z':
            pop, before, after = stack.pop()
            answer[pop] = 'O'
            
            if before == 'head':
                table[after][0] = pop
            elif after == 'tail':
                table[before][1] = pop
            else:
                table[before][1] = pop
                table[after][0] = pop
    
    return ''.join(answer)

