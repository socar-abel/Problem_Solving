def solution(s):
    answer = 1000
    if len(s) == 1 : return 1
    
    for cut in range(1, len(s)//2 + 1):
        cutting = []; i = 0
        
        while i < len(s):
            cutting.append(s[i:i+cut])
            i += cut
        
        # cutting 완료 //
        
        x = 1; count = 0;
        
        while x < len(cutting):
            if cutting[x-1][-cut:] == cutting[x]:
                digit = int(cutting[x-1][:-cut]) if cutting[x-1][:-cut] != "" else 1
                digit += 1
                cutting[x] = str(digit) + cutting[x-1][-cut:]
                cutting[x-1] = 'X'
            x += 1
        
        temp = ""
        for c in cutting:
            if c != 'X': temp += c
        
        if len(temp) < answer : answer = len(temp)
    
    return answer
