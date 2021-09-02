from collections import deque

def timeConvert(time):
    hour = int(time[0:2])
    minute = int(time[3:5])
    return hour * 60 + minute    

def solution(n, t, m, timetable):
    nineOclock = 9 * 60
    busTime = [ nineOclock + (x * t) for x in range(n) ]
    timetable = list(map(lambda x : timeConvert(x), timetable))
    timetable.sort()
    timetable = deque(timetable)
    
    '''
    print('busTime',busTime)
    print()
    print('timetable',timetable)
    print()
    '''
    busPassenger = {x:[] for x in busTime}
    
    for bus in busTime:
        ride = 0
        passenger = []
        while ride < m:
            if not timetable : break
            if timetable[0] <= bus:
                ride += 1; passenger.append(timetable.popleft())
            else: break
        busPassenger[bus] = passenger
        
    #print('busPassenger',busPassenger)    
    
    lastBus = busTime[-1]
    lastBusPassenger = busPassenger[lastBus]
    
    if len(lastBusPassenger) == m: # 꽉 차있으면
        maxValue = max(lastBusPassenger)
        answer = maxValue - 1    
    else:
        answer = lastBus
    
    hour = answer // 60
    minute = answer % 60
    
    if hour < 10 : hour = "0" + str(hour)
    else : hour = str(hour)
    
    if minute < 10 : minute = "0" + str(minute)
    else : minute = str(minute)
    
    return hour + ":" + minute
