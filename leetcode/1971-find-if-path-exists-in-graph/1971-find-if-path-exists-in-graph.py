class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #use dfs, start from the source and do the dfs?
        #if in any point of the traversal you get the destination node return True else False
        # [
        # [0,1]
        # [1,2]
        # [2,0]
        # ]
        visited = set()
        graph = defaultdict(list)
        for a , b in edges: 
            graph[a].append(b)
            graph[b].append(a)
        
        stack = [source]

        while stack: 
            vertex=stack.pop()
            if destination == vertex: 
                return True 
            visited.add(vertex)
            for node in graph[vertex]: 
                if node not in visited: 
                    visited.add(node)
                    stack.append(node)

        return False