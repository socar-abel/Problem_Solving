from itertools import product
from collections import defaultdict

'''
1. alpha_dict 에 알파벳 별 점수 담기
{a: 1, c: 9 ,,}

2. letter_dict 에 letter 별 몇개 담겨 있는지 담기
{a: 2, c: 1, d: 3 ,,}

3. cases 에 word[0], word[1], word[2],, 가 각각 사용될건지 안사용될건지 모든 경우의 수 담기
input 이 작기 때문에 완전탐색해도 시간초과 나지 않음
[(True, True, True, True), (True, True, True, False), ,,]

4. 각 case 에 대해서 점수를 계산해주기
'''


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        answer = 0
        cases = list(product([True, False], repeat=len(words)))
        alpha = "abcdefghijklmnopqrstuvwxyz"
        alpha_dict = defaultdict(int)
        
        for i in range(26):
            alpha_dict[alpha[i]] = score[i]
            
        letter_dict = defaultdict(int)
        for letter in letters:
            letter_dict[letter] += 1
        
        # {True, True, True, Flase}
        for case in cases:
            temp_dict = letter_dict.copy()
            temp_answer = 0

            for i in range(len(case)):
                # 이번 word가 True 라면
                if case[i]:
                    # 진짜 만들 수 있는지 검사
                    word = words[i]
                    word_dict = defaultdict(int)
                    
                    # word_dict {d: 1, o: 1, g: 1}
                    for x in word:
                        word_dict[x] += 1
                    
                    flag = True
                    for key in word_dict.keys():
                        if word_dict[key] > temp_dict[key]:
                            flag = False
                            break
                    
                    # 진짜 만들 수 있으면
                    if flag:
                        for key in word_dict.keys():
                            temp_dict[key] -= word_dict[key]
                    
                        for x in word:
                            temp_answer += alpha_dict[x]
                    else:
                        temp_answer = 0
                        break
                
                if i == len(case) - 1:
                    answer = max(answer, temp_answer)
                
        return answer
        
