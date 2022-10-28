class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        answer = True
        list1 = list(s1)
        list2 = list(s2)
        
        list1.sort()
        list2.sort()                                        
        
        standard = 0
        
        for a, b in zip(list1, list2):
            if a == b:
                continue
            
            if standard == 0:
                if ord(a) > ord(b):
                    standard = 1
                else:
                    standard = 2
            
            # a > b
            if standard == 1:
                if ord(a) < ord(b):
                    answer = False
            
            # a < b
            elif standard == 2:
                if ord(a) > ord(b):
                    answer = False
            
            
        return answer
                
            
            
