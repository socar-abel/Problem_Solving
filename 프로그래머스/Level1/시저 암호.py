def solution(string, n):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    sentence = list(string)
    
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            continue
        elif sentence[i].islower():
            sentence[i] = lower[ (lower.index(sentence[i])+n)%26 ]
        elif sentence[i].isupper():
            sentence[i] = upper[ (upper.index(sentence[i])+n)%26 ]    
    string = "".join(sentence)
    return string
