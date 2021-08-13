def solution(A,B):
    answer = 0
    A.sort(); B.sort();
    
    for _ in range(len(A)):
        answer += A[0] * B[-1]
        A = A[1:]; B = B[:-1]

    return answer
