class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(candidates):
            if not candidates: 
                ans.append(path.copy())

            for candidate in candidates: 
                path.append(candidate) 

                current_candidate = candidates[:]
                current_candidate.remove(candidate)
                backtrack(current_candidate)

                path.pop()
        backtrack(nums)
        return ans 
        
