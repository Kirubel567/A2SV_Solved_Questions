class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        curr = []
        #add the parents for each of the children on the curr and append them to the 
        #create adjecency? 
        # iterate over the adjecencies and create a dictionary of each of the elements of the adjecency list elements as key 
        mapp = defaultdict(list)
        
        for parent, child in edges: 
            mapp[child].append(parent)


        ans = [[] for _ in range(n)]
        def dfs(start_node, curr_node, visited): 
            nonlocal ans
            
            for parent in mapp[curr_node]: 
                if parent not in visited: 
                    visited.add(parent)
                    ans[start_node].append(parent)
                    dfs(start_node, parent, visited)

                

        for i in range(n): 
            visited = set()

            dfs(i, i, visited)

            ans[i].sort()


        return ans 