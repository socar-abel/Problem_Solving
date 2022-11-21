from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequence_set = set()
        tiles = list(tiles)
        N = len(tiles)
        # 몇개로 조합을 만들건지
        for i in range(1, N+1):
            # [(A, B), (A, A)..]
            permu = list(permutations(tiles, i))
            for s in permu:
                sequence_set.add(''.join(s))
        # print(sequence_set)
        return len(sequence_set)
