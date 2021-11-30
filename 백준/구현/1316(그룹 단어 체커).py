from collections import defaultdict
import sys

N = int(sys.stdin.readline())


def check(word):
    alphaDict = defaultdict(int)
    temp = word[0]
    alphaDict[word[0]] += 1

    for s in word[1:]:
        if s == temp: continue
        else:
            if alphaDict[s] >= 1:
                return False
            alphaDict[s] += 1
            temp = s
    return True


answer = 0
for _ in range(N):
    word = sys.stdin.readline().strip()
    if(check(word)): answer += 1

print(answer)

