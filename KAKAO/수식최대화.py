# 많은 것을 배운 문제

# 1. for문을 range(len(list)) 로 돌리면 중간에 삭제가 일어날때 처리 곤란하다.
#   다 끝내고 while문으로 한번 더 거르는 센스. 근데 시간복잡도는 안좋을듯.
#   while op[i] in tempExpression:
# 2. enumerate 내장 함수는 (idx, value) tuple 값을 만들어준다.
# 3. 파이썬에서 리스트 복사는 a = b[:] 슬라이싱으로 이루어져야 한다.

# 맞춘것처럼 보였으나 몇 가지 test case에서 오답이 나왔었다.
# 장하다 상우야 결국 해결함.
# 같은 연산 3개가 연속으로 나올 때가 문제 였음.

from itertools import permutations
def solution(expression):
    answer = 0
    
    expression = expression.replace('+',' + ').replace('-',' - ').replace('*',' * ')
    expression = expression.split(' ')
    
    #print(expression)
    oper = []
    if '+' in expression:
        oper.append('+')
    if '-' in expression:
        oper.append('-')
    if '*' in expression:
        oper.append('*')
    
    # 나올 수 있는 연산자 우선순위 리스트
    # operPermu = [('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'), ('-', '*', '+'), ('*', '+', '-'), ('*', '-', '+')]
    operPermu = list(permutations(oper,len(oper)))
    # print(operPermu)
    
    for op in operPermu:    # ('+', '-', '*')
        # print('op',op) ('+', '-', '*')
        # print(len(op)) 3
        #print('op',op)
        # 파이썬에서는 초기화가 되는 것이 아님 !! 반드시 슬라이싱을 활용해야 함
        tempExpression = expression[:]
        
        for i in range(len(op)):    # ('+', '-', '*')
            print('temp',op[i],tempExpression)
            
            while op[i] in tempExpression:
            
                for idx, value in enumerate(tempExpression):

                    if value == op[i]:

                        tempStr = tempExpression[idx-1] + tempExpression[idx] + tempExpression[idx+1]
                        #print('여기주목',tempExpression[idx-1],tempExpression[idx],tempExpression[idx+1])
                        tempResult = eval(tempStr)
                        print('tempResult',tempResult)
                        del tempExpression[idx-1:idx+2]
                        #print('del 체크:',tempExpression)
                        tempExpression.insert(idx-1,str(tempResult))
                        break
                    
                    
                    
        # print('after',tempExpression)
        result = ''.join(tempExpression)
        result = abs(eval(result))
        print('result',result)
        print()
        if result >= answer:
            answer = result
        
                    
            
            
    # print(expression)
    
    return answer
