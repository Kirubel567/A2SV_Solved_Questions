class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        seen = set()
        def backtrack(candidates): 
            for i in range(len(candidates)): 
                path.append(candidates[i])
                backtrack(candidates[i+1:])
                path.pop()
            else: 
                if tuple(sorted(path)) not in seen:  
                    ans.append(path.copy())
                    seen.add(tuple(sorted(path)))

        backtrack(nums)
        return ans 
            
