a, b = map(int, input().strip().split(' '))
for _ in range(b):
    for _ in range(a):
        print("*",end = '')
    print()
    
# 더 쉬운 풀이
a, b = map(int, input().strip().split(' '))
print(("*"*a+'\n')*b)
