def solution(s):
    answer = ''; words = []; i = 0
    while True:
        if i >= len(s) : break
        if s[i] == ' ' : words.append(' '); i += 1
        else : 
            temp = ''
            while i < len(s) and s[i] != ' ':
                temp += s[i]; i += 1
            words.append(temp)
    
    for word in words:
        if word == ' ' : answer += ' '
        else : answer += word[0].upper() + word[1:].lower()
    
    return answer
