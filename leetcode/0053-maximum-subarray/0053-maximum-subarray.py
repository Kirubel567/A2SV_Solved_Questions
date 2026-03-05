class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _sum, ans = 0, nums[0]

        for i in range(len(nums)): 
            if _sum < 0: 
                _sum = 0
            _sum += nums[i]
            ans = max(ans, _sum)
        
        return ans 