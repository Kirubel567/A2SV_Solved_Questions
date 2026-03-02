class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        _sum = 0
        return [_sum := _sum + nums[i] for i in range(len(nums))] 