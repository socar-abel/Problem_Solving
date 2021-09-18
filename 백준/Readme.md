## BaekJoon Online Judge 
### 알고리즘 별 연습
1. BSF / DFS
2. 그리디
3. DP (Dynamic Programming)
4. 백트래킹
5. 이진 탐색
6. 위상 정렬
### 알고리즘 팁
### 1. Recursion Error 해결법
재귀 함수 호출이 1000번으로 제한 걸려있기 때문에 리밋 해제를 해줘야한다.   

```python
import sys
sys.setrecursionlimit(10000000)
```

### 2. input() 빨리 받기
아래가 더 빠른 코드.   
```python
N, M = map(int, input().split())

N, M = map(int, sys.stdin.readline().split())
```

### 3. 런타임에러(Index Error)
```python
map(input().split())
map(input())
```
split()이 필요없을 때 해줬을 시 Index Error가 난다. 
## 복습할 문제들 🙄
- 1013 Contact
- 1520 내리막길
