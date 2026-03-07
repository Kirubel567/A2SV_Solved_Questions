class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        #this question is a bit similar with coorporate flight
        pref_sum = [0]*(len(nums)+1)

        for start, end in requests: 
            pref_sum[start] += 1
            pref_sum[end+1] -= 1
        
        for i in range(1, len(pref_sum)): 
            pref_sum[i] += pref_sum[i-1]
        
        nums.sort()
        pref_sum = pref_sum[:-1]
        pref_sum.sort()

        sumCounter = 0
        for i in range(len(nums)): 
            sumCounter += nums[i] * pref_sum[i]

        return sumCounter % 1000000007