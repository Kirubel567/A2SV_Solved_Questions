class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(candidates, prev): 

            for i in range(len(candidates)): 
                if prev <= candidates[i]: 
                        path.append(candidates[i])
                        
                        if len(path)>1 and path not in ans:
                            ans.append(path[:])

                        backtrack(candidates[i+1:], candidates[i])
                        path.pop()

        backtrack(nums, float('-inf'))
        return ans 