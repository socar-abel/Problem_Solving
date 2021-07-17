def solution(s):
    string = list(s)
    index = 0
    
    for i in range(len(string)):
        if string[i] == ' ':
            index = 0
            continue
        else:
            if index % 2 == 0:
                string[i] = string[i].upper()
                index += 1
            else:
                string[i] = string[i].lower()
                index += 1    
    
    return "".join(string)
