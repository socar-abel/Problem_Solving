import heapq

def solution(scoville, K):
    heapq.heapify(scoville) # O(n)에 힙을 생성
    count = 0
    
    while True:
        now = scoville[0] # O(1)에 min값을 얻음
        if now >= K :
            break
        else:
            if len(scoville) == 1 : return -1
            else:
                first = heapq.heappop(scoville)
                second = heapq.heappop(scoville)
                heapq.heappush(scoville,first + second*2)
                count += 1
                
    return count
