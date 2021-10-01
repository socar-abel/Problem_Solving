import sys
N = int(input())

words = [sys.stdin.readline().strip() for _ in range(N)]

# { A:10000, B:1, G:100, ..}
alpha = dict()

for word in words:
    for i in range(len(word)):
        if not word[i] in alpha:
            alpha[word[i]] = 10**(len(word)-i-1)
        else:
            alpha[word[i]] += 10**(len(word)-i-1)

#print(alpha)

result = []
for a in alpha:
    result.append((a,alpha[a]))

result.sort(key=lambda x:x[1],reverse=True)

num = 9
for x, y in result:
    alpha[x] = num
    num -= 1

#print(alpha)

answer = 0
for word in words:
    temp = ""
    for w in word:
        temp += str(alpha[w])
    answer += int(temp)

print(answer)
