def inTime(log, time):  # time 부터 시작한 1초 안에 log가 있는지
    answer = True
    if log[1] < time: answer = False
    if log[0] > time + 999: answer = False
    
    return answer

def solution(lines):
    answer = 0
    logs = []
    throughputs = dict()
    
    for line in lines:
        # parsing
        hour = int(line[11:13]); minute = int(line[14:16]); second = float(line[17:23])
        end = int(hour*3600*1000 + minute*60*1000 + second*1000)
        # 처리시간 T
        T = int(float(line[24:-1])*1000)
        start = end - T + 1
        # Log 저장
        logs.append( (start,end) )
        # 시간당 처리량
        throughputs[start] = 0
        throughputs[end] = 0
        
    for key in throughputs:
        x = 0
        for log in logs:
            if inTime(log, key): x += 1
        throughputs[key] = x
    
    answer = max(throughputs.values())
    print(throughputs)
    
    return answer


