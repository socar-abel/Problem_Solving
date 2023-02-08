import Foundation

let n = Int(readLine()!)!
var fibo = Array(repeating: 0, count: n+1)

if n == 0
{
    print(0)
}
else if n == 1
{
    print(1)
}
else if n == 2
{
    print(1)
}
else if n >= 3
{
    fibo[0] = 0
    fibo[1] = 1
    fibo[2] = 1
    for i in 3...n
    {
        fibo[i] = fibo[i-1] + fibo[i-2]
    }
    print(fibo[n])
}

