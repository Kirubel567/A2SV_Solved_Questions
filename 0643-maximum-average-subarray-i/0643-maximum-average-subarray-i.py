class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = sum(nums[:k])/k
        _sum = sum(nums[:k])
        left = 0
        for r in range(k, len(nums)): 
            _sum += (nums[r] - nums[left])
            max_avg = max(max_avg, _sum/k)
            left+=1
            
        return max_avg
