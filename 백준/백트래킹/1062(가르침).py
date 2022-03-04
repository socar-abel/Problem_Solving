from itertools import combinations
import sys
alphabet = list('bdefghjklmopqrsuvwxyz')
N, K = map(int, sys.stdin.readline().split())
words = []
for _ in range(N):
    words.append(sys.stdin.readline().strip())

# 필수 단어 5개는 꼭 배워야 한다.
if K < 5:
    print(0)
    sys.exit(0)


def howManyWordsCanLearn(teach_alpha_list):
    result = 0
    for word in words:
        canLearn = True
        for x in word:
            if x not in teach_alpha_list:
                canLearn = False
                break
        if canLearn:
            result += 1

    return result


basic = ['a', 'n', 't', 'c', 'i']
combs = list(combinations(alphabet, K-5))

answer = 0
for comb in combs:
    teach_alphabet = basic + list(comb)
    answer = max(answer, howManyWordsCanLearn(teach_alphabet))

print(answer)
