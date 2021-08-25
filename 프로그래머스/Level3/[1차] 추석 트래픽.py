def parsing(line):
    end = int(line[11:13]) * 3600 * 1000 + int(line[14:16]) * 60 * 1000
    millis = int(line[17:19] + line[20:23])
    end += millis
    second = int(float(line[24:-1]) * 1000)
    return end, second

def check(start, end, time1, time2):
    if start <= time1 and end >= time1 : return True
    elif time1 <= start <= time2 : return True
    else : return False

def solution(lines):
    answer = 0
    stamps = []
    
    for line in lines:  # O(N)
        end, sec = parsing(line)
        start = end - sec + 1
        stamps.append((start,end))
    
    stamps.sort(key = lambda x : x[0])
    results = [1]
    
    for i in range(len(stamps)): # O(N)
        time = stamps[i][0]; j = 0; result = 0
        while True: # O(N)
            if j >= len(stamps) or stamps[j][0] > time + 999 : break
            if check(stamps[j][0], stamps[j][1], time, time + 999):
                result += 1
            j += 1
        results.append(result)
        
        time2 = stamps[i][1]; k = 0; result2 = 0
        while True:
            if k >= len(stamps) or stamps[k][0] > time2 + 999 : break
            if check(stamps[k][0], stamps[k][1], time2, time2 + 999):
                result2 += 1
            k += 1
        results.append(result2)
    
    return max(results)
