# 파이썬 정규표현식 개사기
import re
T = int(input())

signals = []
for _ in range(T):
    signals.append(input())

for signal in signals:
    p = re.compile('(100+1+|01)+')
    result = p.fullmatch(signal)
    if result:
        print('YES')
    else:
        print('NO')
