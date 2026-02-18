class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mapp = {}
        sorted_nums = sorted(nums)
        #1, 2, 2, 3, 8
        for i in range(len(nums)):
            #jump the repeated number
            if sorted_nums[i] in mapp: 
                continue 
            mapp[sorted_nums[i]] = i

        ans = [mapp[num] for num in nums]
        return ans