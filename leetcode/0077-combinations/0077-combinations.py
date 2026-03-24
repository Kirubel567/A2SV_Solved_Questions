class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        ans = []

        def backtrack(start): 
            if len(path) == k: 
                ans.append(path[:])
                return 

            #create the candidates???
            candidates = [i for i in range(start+1, n+1)]
            
            for i in range(len(candidates)): 
                path.append(candidates[i])

                backtrack(candidates[i])
        
                path.pop()
        backtrack(0)
        return ans 