class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        #stk = [1,2] float('inf')
        #3 is min between -1 and 1 exclusive
        #1 is min between -1 and 6 exclusive(0-5) exclusive 
        #2 is min between 6 and 1 exclusive
        #4 is min between 5 and 1 exclusive
        #5 is min between 4 and 1 exclusive
        #6 is min between 4 and 2 exclusive
        #2 is min between 6 and 4 exclusive
        #find the sum of each elements subarray where the element is the smallest 


        #use prefix sum not to make the operation of getting _sum n^2
        pref = [0]
        for i in range(len(nums)): 
            pref.append(pref[-1] + nums[i])

        nums.append(float('-inf')) #for taking care of the elements remaining in the stk
        stk = []
        ans = -float('inf')
        
        for i, num in enumerate(nums): 
            while stk and nums[stk[-1]] >= num: 
                #calculate for the specific subarray 
                curr = stk.pop()
                left = stk[-1] if stk else -1
                right = i
                _sum = pref[right] - pref[left+1] #exclusive of the two ends(the ones that are greater)
                ans = max(ans, _sum*nums[curr])
            stk.append(i)
        return ans % (10**9+7)
