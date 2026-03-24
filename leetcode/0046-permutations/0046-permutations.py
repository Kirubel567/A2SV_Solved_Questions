class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(candidates):
            if not candidates: 
                ans.append(path.copy())

            for i in range(len(candidates)): 
                path.append(candidates[i]) 

                backtrack(candidates[:i]+candidates[i+1:])

                path.pop()
        backtrack(nums)
        return ans 
        
