def solution(people, limit):
    answer = 0
    
    people.sort()
    minV = people[0]
    cut = 0
    
    for idx in range(len(people)):
        if limit - minV < people[idx] : 
            cut = idx
            break
    
    can_2_people = people[:cut]
    can_1_people = people[cut:]
    
    #print(can_2_people)
    
    share_index = []
    l = len(can_2_people)
    left, right = 0, l-1
    while left < right:
        
        if can_2_people[left] + can_2_people[right] <= limit:
            share_index.append(left)
            share_index.append(right)
            left += 1
            right -= 1
        else : 
            right -= 1
    
    #print(share_index)
    
    answer = len(can_1_people) + len(can_2_people) - len(share_index) // 2
    
    return answer
