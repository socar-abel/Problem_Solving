def divide(file):
    i = 0
    head, number, tail = '','',''
    while not file[i].isdigit():
        head += file[i]; i += 1
    count = 0
    while i < len(file) and file[i].isdigit() and count < 5:
        number += file[i]; i += 1; count += 1
    while i < len(file):
        tail += file[i]; i += 1
    head = head.upper()
    number = int(number)
    return (head, number, tail)

def solution(files):
    answer = []
    myFiles = []
    for i in range(len(files)):
        file = files[i]
        d = (divide(file)[0],divide(file)[1],divide(file)[2],file,i)
        myFiles.append(d)
    myFiles.sort(key = lambda x : (x[0],x[1],x[4]))
    
    for x in myFiles:
        answer.append(x[3])
        
    return answer
