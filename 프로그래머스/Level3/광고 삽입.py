def solution(play_time, adv_time, logs):
    answer = ''
    playtime = s2i(play_time) + 1
    advtime = s2i(adv_time)
    print(advtime)
    cnt = [0] * playtime
    start = [0] * playtime
    end = [0] * playtime

    for log in logs:
        s, e = log.split('-')
        s = s2i(s)
        e = s2i(e)
        start[s] += 1
        end[e] += 1

    cnt[0] = start[0] - end[0]
    for i in range(1, playtime):
        d = start[i] - end[i]
        cnt[i] = cnt[i-1] + d

    window = 0
    maxV = 0

    for i in range(advtime):
        window += cnt[i]

    #print(window)

    if maxV < window:
        answer = i2s(0)
        maxV = window
    #print(window, answer)

    for i in range(advtime, playtime):
        window = window - cnt[i - advtime] + cnt[i]

        if maxV < window:
            answer = i2s(i - advtime + 1)
            #print('answer', answer)
            #print('window', window)
            maxV = window

    return answer


def s2i(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s


def i2s(time):
    h = str(time // 3600)
    m = str((time % 3600) // 60)
    s = str((time % 3600) % 60)
    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
    if len(s) == 1:
        s = '0' + s
    return h + ':' + m + ':' + s


