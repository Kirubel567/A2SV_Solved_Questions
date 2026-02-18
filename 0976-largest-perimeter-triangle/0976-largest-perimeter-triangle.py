class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #1, 1, 2, 10
        #1, 2, 2
        nums.sort()
        ans = 0
        for i in range(len(nums)-1, 1, -1): 
            Sum = nums[i] + nums[i-1]+nums[i-2]
            if nums[i] < nums[i-1]+nums[i-2]: 
                ans = max(ans, Sum)
        return ans 
