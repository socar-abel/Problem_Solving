class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        n = len(graph)

        def dfs(node, path):
            if node == n-1:
                answer.append(path)
                return

            for x in graph[node]:
                dfs(x, path+[x])

        dfs(0, [0])
        return answer
