# two pointers with while loop

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            si = firstList[i][0]
            ei = firstList[i][1]
            sj = secondList[j][0]
            ej = secondList[j][1]

            s = max(si, sj)
            e = min(ei, ej)

            if s <= e:
                answer.append([s, e])
            
            if ei <= ej:
                i += 1
            else:
                j += 1

        
        return answer

