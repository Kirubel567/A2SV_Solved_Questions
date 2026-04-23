class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE=0
        BLACK=1
        GREY=2
        
        Color = {k: WHITE for k in range(numCourses)}
        cycle = False

        adj_list = defaultdict(list)

        #create the adjacency list here 
        for a, b in prerequisites: 
            adj_list[b].append(a)
        
        def dfs(node): 
            nonlocal cycle 
            if Color[node] == GREY: 
                return True 
            if Color[node] == BLACK: 
                return False
            

            Color[node] = GREY
            if node in adj_list: 
                for nei in adj_list[node]: 
                    if dfs(nei): 
                        return True

            Color[node] = BLACK
            return False
        
        for node in adj_list: 
            if dfs(node): 
                return False
        
        return True 