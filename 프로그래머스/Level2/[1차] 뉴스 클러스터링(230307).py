from collections import defaultdict

def solution(str1, str2):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = 0
    # dictA = {FR : 1, RA : 1, AN : 1 ,...}
    dictA = defaultdict(int)
    dictB = defaultdict(int)

    for i in range(len(str1)-1):
        word = str1[i:i+2].upper()
        flag = True
        for w in word:
            if w not in alphabet:
                flag = False
                break
        if flag:
            dictA[word] += 1

    for i in range(len(str2)-1):
        word = str2[i:i + 2].upper()
        flag = True
        for w in word:
            if w not in alphabet:
                flag = False
                continue
        if flag:
            dictB[word] += 1

    key_set = set()
    for k1 in dictA:
        key_set.add(k1)
    for k2 in dictB:
        key_set.add(k2)
        
    inter = 0
    add = 0
    for key in list(key_set):
        if key in dictA and key in dictB:
            inter += min(dictA[key], dictB[key])
            add += max(dictA[key], dictB[key])
        elif key in dictA:
            add += dictA[key]
        elif key in dictB:
            add += dictB[key]

    jakad = (inter/add) if add != 0 else 1

    return int(jakad*65536)
