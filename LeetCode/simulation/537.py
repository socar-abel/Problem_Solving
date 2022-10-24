class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.replace('i', '+')
        num2 = num2.replace('i', '+')
        
        s1 = num1.split('+')
        s2 = num2.split('+')
        
        real1, img1 = int(s1[0]), int(s1[1])
        real2, img2 = int(s2[0]), int(s2[1])
        
        ans_real = real1 * real2 - img1 * img2
        ans_img = real1 * img2 + real2 * img1
        
        return str(ans_real) + '+' + str(ans_img) + 'i'
