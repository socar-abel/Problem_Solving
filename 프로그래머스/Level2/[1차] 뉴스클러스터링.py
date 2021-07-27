def solution(str1, str2):
    answer = 0
    list1 = [str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    list2 = [str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    if not list1 and not list2 : return 65536
    
    dic1 = { x:list1.count(x) for x in list1 }
    dic2 = { x:list2.count(x) for x in list2 }
     
    #print(dic1,dic2)
                    
    intersection = []
    for key in dic1.keys():
        if key in dic2.keys():
            for _ in range(min(dic1[key],dic2[key])):
                intersection.append(key)
    #print(intersection)        
            
    return int(( len(intersection)/(len(list1)+len(list2)-len(intersection)) ) * 65536)
