
from string import ascii_uppercase

def solution(name):
    answer = 0
    making = list("A"*len(name))
    alphabet = list(ascii_uppercase)
    
    cursor = 0
    while "".join(making) != name:
        #print('making',making)
        cursor = cursor % len(name)
        #print('cursor',cursor)
        #print('while1')
        # "AAA" vs "JAN"
        if making[cursor] != name[cursor]:
            # 상하 이동
            #print('상하이동')
            upDown = min(alphabet.index(name[cursor]) , alphabet[::-1].index(name[cursor])+1)
            answer += upDown
            making[cursor] = name[cursor]
        #print('making2',making)        
        # 좌우 커서 이동
        move = 0
        while True:
            if "".join(making) == name : break
            #print('while2')
            #print('making[cursor]',making[cursor])
            if making[ (cursor+move) % len(name) ] != name[ (cursor+move) % len(name) ]:
                #print(1)
                cursor += move
                break
            elif making[ (cursor-move) % len(name) ] != name[ (cursor-move) % len(name) ]:
                #print(2)
                cursor -= move
                break
            move += 1
        
        answer += move
            
    
    return answer

# print(solution("JEROEN"))
