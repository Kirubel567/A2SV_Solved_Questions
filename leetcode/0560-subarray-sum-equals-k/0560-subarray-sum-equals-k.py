class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum = defaultdict(int)
        pref_sum[0] = 1

        _sum, count = 0, 0
        for i in range(len(nums)): 
            _sum += nums[i]

            count += pref_sum[_sum-k]
            pref_sum[_sum] += 1
        return count 