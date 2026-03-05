class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1} #init with 0:-1 not to return on the first multiple(we need atleast two elements in the subarray)

        total = 0
        for i in range(len(nums)): 
            total += nums[i]
            r = total % k

            if r not in remainder: 
                remainder[r] = i
            elif i - remainder[r]>1: 
                return True 
        return False 

        #the idea is that if a remainder is repeated in the prefix sum then in between the two repeating remainders there exists a multiple of k
