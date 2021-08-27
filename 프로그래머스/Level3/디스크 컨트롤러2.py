# 전에 블로그 보고 따라해봤지만, 더 좋은 코드를 작성해보았다.
import heapq
def solution(jobs):
    total = 0
    time = 0; i = 0; start = -1; waiting = []
    jobs.sort(key = lambda x : x[0])
    while i < len(jobs):
        for job in jobs[i:]:  # 이 부분이 다름
            if start < job[0] <= time:
                heapq.heappush(waiting, (job[1], job[0]))
        if waiting:
            pop = heapq.heappop(waiting)
            start = time
            time += pop[0]
            total += time - pop[1]
            i += 1
        else:
            time += 1
    
    return total // len(jobs)
