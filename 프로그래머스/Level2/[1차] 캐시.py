from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0 : return len(cities) * 5
    answer = 0
    cache = deque()
    
    for city in cities:
        city = city.upper()
        
        if len(cache) < cacheSize:
            if city in cache : answer += 1
            else : answer += 5
            cache.append(city)
        else :
            if city in cache : 
                cache.remove(city)
                cache.append(city)
                answer += 1
            else : 
                answer +=5 
                cache.popleft(); cache.append(city)

    return answer
