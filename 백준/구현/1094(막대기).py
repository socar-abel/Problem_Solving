import sys
X = int(sys.stdin.readline())

stick = 64
unit = [64]

while True:
    if stick == X:
        print(len(unit))
        break

    unit.sort()
    minUnit = min(unit)
    cut = minUnit // 2

    tempSum = sum(unit[1:]) + cut
    if tempSum >= X:
        unit[0] = cut
        stick = tempSum
    else:
        unit[0] = cut
        unit = [cut] + unit
        stick = stick


