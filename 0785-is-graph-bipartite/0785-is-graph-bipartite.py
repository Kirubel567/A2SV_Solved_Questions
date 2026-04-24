class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(i, c):
            color[i] = c
            for j in graph[i]:
                if j in color:
                    if color[j] == c:
                        return False
                    continue
                elif not dfs(j, 1 - c):
                    return False
            return True

        for x in range(len(graph)):
            if x not in color:
                if not dfs(x, 0):
                    return False
        return True