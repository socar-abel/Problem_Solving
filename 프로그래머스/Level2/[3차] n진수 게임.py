import string

tmp = string.digits+string.ascii_uppercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    answer = ''
    string = ''
    total = m * (t-1) + p
    x = 0
    while True:
        if len(string) > total : break
        temp = convert(x,n)
        #print('temp',temp)
        string += temp
        x += 1
    
    for i in range(len(string)):
        #print('answer',answer)
        if len(answer) == t : break
        if m == p : 
            if (i+1) % m == 0 : answer += string[i]
        else:
            if (i+1) % m == p : answer += string[i]
        

    return answer

