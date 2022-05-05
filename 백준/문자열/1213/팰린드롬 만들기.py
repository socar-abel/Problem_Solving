from collections import defaultdict
import sys
S = sys.stdin.readline().strip()
impossible = "I'm Sorry Hansoo"
alpha = defaultdict(int)

for i in range(len(S)):
    alpha[S[i]] += 1


# 문자열 길이가 홀수라면, 개수가 홀수인 알파벳은 한개여야 한다.
if len(S) % 2 == 1:
    odd = 0
    for key in alpha:
        if alpha[key] % 2 == 1:
            odd += 1
        if odd > 1:
            print(impossible)
            sys.exit(0)

    # 팰린드롬을 만들 수 있는 경우
    keys = list(alpha.keys())
    keys.sort()

    left = ""
    odd_alpha = 'x'
    for key in keys:
        if alpha[key] % 2 == 0:
            left += key * (alpha[key] // 2)
        else:
            left += key * (alpha[key] // 2)
            odd_alpha = key

    answer = left + odd_alpha + left[::-1]
    print(answer)

# 문자열 길이가 짝수라면, 개수가 홀수인 알파벳은 없어야 한다.
else:
    odd = 0
    for key in alpha:
        if alpha[key] % 2 == 1:
            odd += 1
        if odd >= 1 :
            print(impossible)
            sys.exit(0)

    # 팰린드롬을 만들 수 있는 경우
    keys = list(alpha.keys())
    keys.sort()

    left = ""
    for key in keys:
        left += key * (alpha[key] // 2)

    answer = left + left[::-1]
    print(answer)
