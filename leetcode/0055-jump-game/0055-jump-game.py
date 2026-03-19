class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = float('-inf')
        for i in range(len(nums)): 
            if farthest!= float('-inf') and i > farthest:
                break

            farthest = max(farthest, nums[i]+i)
        print(farthest)
        return True if farthest >= len(nums)-1 else False