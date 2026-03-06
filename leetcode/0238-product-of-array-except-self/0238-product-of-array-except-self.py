class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #if there is a zero every other elemnts will be zero except for the position where the zero is found 
        #calculate the total product when the elemtn is zero just skip it don't put it in the product 
        #iterate over the elements again and ans[i] = total_prod/nums[i] if zero is found in the array then at zero's position pos ans[pos] = total_prod, the make all the rest zero 
        total_prod = 1
        ans = [0]*len(nums)
        passed = False

        for i in range(len(nums)): 
            if nums[i] == 0: 
                continue 
            
            total_prod *= nums[i]
            passed = True 
        if 0 in nums: 
            for i in range(len(nums)): 
                if nums[i] == 0: 
                    ans[i] = total_prod if (total_prod != 1 or passed) and nums.count(0) == 1 else 0
        else: 
            for i in range(len(nums)): 
                ans[i] = total_prod//nums[i]
        return ans 
        