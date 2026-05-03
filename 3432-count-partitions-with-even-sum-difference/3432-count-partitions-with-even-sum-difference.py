class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        accumulate, count = 0, 0
        for i in range(len(nums)-1): 
            accumulate += nums[i]
            if (accumulate - (total_sum - accumulate))%2==0: 
                count += 1
            
        return count  
