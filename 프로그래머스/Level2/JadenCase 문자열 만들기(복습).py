# 나 예전에 뭐 이렇게 어렵게 푼거지 ..;

def solution(s):
    answer = ''
    words = s.split(' ')
    
    for word in words:
        if word: answer += word[0].upper() + word[1:].lower() + ' '
        else: answer += ' '

    return answer[:-1]
