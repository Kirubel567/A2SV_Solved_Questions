class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        stk = []

        for i in range(len(nums)*2): 
            idx = i%len(nums)
            while stk and nums[stk[-1]] < nums[idx]: 
                ans[stk.pop()] = nums[idx]
            if i < len(nums):
                stk.append(idx)
        return ans 
        