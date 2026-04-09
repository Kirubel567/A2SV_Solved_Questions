class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(curr): 
            if len(path) == k: 
                ans.append(path[:])
                return 
            
            for candidate in range(curr+1, n+1): 
                path.append(candidate)
                backtrack(candidate)
                path.pop()
            else: 
                return 

        backtrack(0)
        return ans 