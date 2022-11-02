class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # (p, g)
        pg = [(x, y) for x, y in zip(plantTime, growTime)]
        pg.sort(key=lambda x: -x[1])
        
        answer = pg[0][0] + pg[0][1]
        p_time = pg[0][0]
        
        for i in range(1, len(pg)):
            answer = max(answer, p_time + pg[i][0] + pg[i][1])
            p_time += pg[i][0]
        
        return answer
            
