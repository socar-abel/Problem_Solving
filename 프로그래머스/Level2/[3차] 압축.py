from string import ascii_uppercase
dictionary = {}

def find(msg):
    global dictionary
    i, w = 0, ''
    while True:
        if i >= len(msg) : break
        if msg[:i+1] in dictionary : 
            w = msg[:i+1]; i += 1
        else : break
    return w

def solution(msg):
    answer, i = [], 1
    global dictionary
    # step1
    for alphabet in list(ascii_uppercase):
        dictionary[alphabet] = i; i += 1

    while True:
        # step2
        w = find(msg)
        #print('w',w)
        # step3
        answer.append(dictionary[w])
        if len(w) == len(msg) : break
        else : msg = msg[len(w):]; #print('changed msg',msg)
        # step4
        dictionary[w+msg[0]] = len(dictionary) + 1

    #print(dictionary)
    return answer
