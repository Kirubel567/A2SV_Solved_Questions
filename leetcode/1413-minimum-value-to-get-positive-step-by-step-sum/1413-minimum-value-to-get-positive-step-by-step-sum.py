class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        _sum = 0 
        startValue = -float('inf')
        for num in nums: 
            _sum += num 
            if _sum < 0: 
                startValue = max(startValue, abs(_sum)+1)
        return startValue if startValue != -float('inf') else 1