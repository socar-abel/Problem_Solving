# AI 문자인식 결과 elements
# 로직만 Python 으로 먼저 짜봤다. Swift 로 변경해야 함

resultElements = [["ksw", "-", "+++", "O80", "-", "1234-5", "678"],
                  ["bsj", "ㅇ8O-1234", "5678"],
                  ["080", "-", "1111", "-", "2222", "ksw", "12345678"],
                  ["0101", "훼이크", "080", "응 아니야", "080", "-", "123", "-", "4567"]]

confusingWithZero = ['o', 'O', 'ㅇ']


def isConsideredAsNumber(x):
    if (x in ['o', 'O', 'ㅇ', '-', '.']) or x.isdigit():
        return True
    else:
        return False


def elemIsNumber(elem):
    result = True
    for x in elem:
        if not isConsideredAsNumber(x):
            result = False
            break
    return result


def refineElemNumber(number):
    result = ""
    for x in number:
        if x.isdigit():
            result += x
        elif x in ['o', 'O', 'ㅇ']:
            result += "0"
    return result


def getTELNumber(elements):
    for element in elements:
        answer = ""
        for elem in element:
            if elemIsNumber(elem):
                answer += refineElemNumber(elem)
            else:
                answer = ""

            if 10 <= len(answer) <= 11:
                break

        print(answer)


getTELNumber(resultElements)


