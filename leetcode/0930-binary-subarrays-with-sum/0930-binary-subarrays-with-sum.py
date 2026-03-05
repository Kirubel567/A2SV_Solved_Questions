class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        _sum, count = 0, 0 
        for i in range(len(nums)): 
            _sum += nums[i]

            count += prefix_sum[_sum-goal]

            prefix_sum[_sum] += 1
        return count 
