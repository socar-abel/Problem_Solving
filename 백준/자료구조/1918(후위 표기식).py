from collections import defaultdict
import sys
formula = list(sys.stdin.readline().strip())

alphabetStack = []
operatorStack = []


def isNowStronger(now, t):
    operator = ['?', '(', '+', '-', '*', '/']
    scoreNow = operator.index(now) // 2
    scoreTop = operator.index(t) // 2
    return scoreNow > scoreTop


for x in formula:
    if x.isalpha():
        alphabetStack.append(x)
    else:
        if not operatorStack:
            operatorStack.append(x)
        else:
            if x == '(':
                operatorStack.append(x)
            elif x == ')':
                while operatorStack[-1] != '(':
                    top = operatorStack.pop()
                    one = alphabetStack.pop()
                    two = alphabetStack.pop()
                    alphabetStack.append(two + one + top)

                operatorStack.pop()
            else:
                if isNowStronger(x, operatorStack[-1]):
                    operatorStack.append(x)
                else:
                    while operatorStack and not isNowStronger(x, operatorStack[-1]):
                        top = operatorStack.pop()
                        one = alphabetStack.pop()
                        two = alphabetStack.pop()
                        alphabetStack.append(two + one + top)
                    operatorStack.append(x)

while operatorStack:
    nowOperator = operatorStack.pop()
    one = alphabetStack.pop()
    two = alphabetStack.pop()
    alphabetStack.append(two + one + nowOperator)

print(alphabetStack[0])
