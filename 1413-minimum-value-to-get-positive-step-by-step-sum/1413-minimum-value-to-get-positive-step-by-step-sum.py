class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = float('inf')
        accumulate = 0
        for i in range(len(nums)): 
            accumulate += nums[i]

            min_sum = min(min_sum, accumulate)
        return max(1, 1-min_sum)