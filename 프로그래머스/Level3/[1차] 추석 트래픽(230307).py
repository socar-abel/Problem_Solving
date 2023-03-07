def convert_to_millisecond(s):
    day, time, play_time = s.split(' ')
    hour, minute, second = time.split(':')
    _second = second.replace('.', '')
    millisecond = int(_second) + int(int(minute) * 60 * 1000) + int(int(hour) * 60 * 60 * 1000)
    T = float(play_time[:-1])
    return millisecond, int(T*1000)



def solution(lines):
    answer = 0
    events = []

    for line in lines:
        S, T = convert_to_millisecond(line)
        events.append((S-T+1, S))

    events.sort(key=lambda x: (x[0], x[1]))

    for i in range(len(events)):
        i_start, i_end = events[i]
        for s in [i_start, i_end]:
            temp_answer = 0
            for j in range(len(events)):
                j_start, j_end = events[j]
                if s <= j_end and j_start <= s + 999:
                    temp_answer += 1
            answer = max(answer, temp_answer)
            
    return answer
