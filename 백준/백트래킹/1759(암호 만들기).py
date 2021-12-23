import sys
sys.setrecursionlimit(10**6)
L, C = map(int, sys.stdin.readline().split())
alphabet = list(sys.stdin.readline().split())
mo = ['a', 'e', 'i', 'o', 'u']  # 모음
alphabet.sort()


def check(word):
    moEum = 0
    jaEum = 0
    for w in word:
        if w in mo:
            moEum += 1
        else:
            jaEum += 1

    return moEum, jaEum


def dfs(idx, word):
    word += alphabet[idx]
    result = check(word)
    if len(word) == L:
        if result[0] >= 1 and result[1] >= 2:
            print(word)
        return

    for i in range(idx+1, C):
        dfs(i, word)


for x in range(C):
    dfs(x, "")
