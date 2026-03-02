class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        #create a inclusive pre_fix and exclusive post_fix 
        pre_fix = []
        accumulate = 0
        for i in range(len(nums)):
            accumulate += nums[i]
            pre_fix.append(accumulate)

        accumulate, count = 0, 0
        post_fix = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1): 
            post_fix[i] = accumulate
            accumulate += nums[i]

        for i in range(len(nums)-1): 
            if (pre_fix[i] - post_fix[i])%2==0: 
                count += 1

        return count
