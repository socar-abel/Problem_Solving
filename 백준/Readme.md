## BaekJoon Online Judge
### 알고리즘 별 연습
1. BSF / DFS
2. 그리디
3. 백트래킹
4. 이진 탐색
5. 위상 정렬
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

