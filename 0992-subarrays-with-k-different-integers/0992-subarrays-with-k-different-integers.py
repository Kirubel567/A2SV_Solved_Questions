class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        #initialize a map to store the freq of each elem
        #iterate over the array and if len(mapp) > k then move the left pointer(shrink the window) then count += 1
        freq = defaultdict(int)
        left_near = left_far = count = 0
        for r in range(len(nums)): 
            freq[nums[r]]+=1

            while len(freq) > k:
                freq[nums[left_near]] -= 1
                if freq[nums[left_near]]==0:
                    freq.pop(nums[left_near]) 
                left_near += 1
                left_far = left_near
            while freq[nums[left_near]] > 1: 
                freq[nums[left_near]]-=1
                left_near+=1
            
            if len(freq) == k: 
                count += left_near - left_far +1
            
        return count
        
            