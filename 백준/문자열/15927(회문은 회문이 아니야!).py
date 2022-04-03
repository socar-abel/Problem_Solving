import sys
s = sys.stdin.readline().strip()
t = s[::-1]
palindrome = True

for i in range(len(s)):
    if s[i] != t[i]:
        palindrome = False

if not palindrome:
    print(len(s))
else:
    all_same = True
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            all_same = False

    if all_same:
        print(-1)
    else:
        print(len(s) - 1)

