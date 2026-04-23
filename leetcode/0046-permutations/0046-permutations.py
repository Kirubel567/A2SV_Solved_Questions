class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path =[]
        ans = []
        def backtrack(candidates): 
            if len(path) == len(nums): 
                ans.append(path.copy())
                return

            for i in range(len(candidates)): 
                path.append(candidates[i])
                backtrack(candidates[:i]+candidates[i+1:])
                path.pop()
        
        backtrack(nums)
        return ans 
