class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        #use monotonic queue, one increasing and the other decreasing,
        #increasing to keep the min element in the current subarray and dec for max
        #use queue instead of stack as we need to remove elements from the front 
        _max = deque()
        _min = deque()
        ans = float('-inf')

        left = 0
        for r in range(len(nums)): 
            while _max and _max[-1][1] < nums[r]: 
                _max.pop()
            _max.append((r, nums[r]))
            while _min and _min[-1][1] > nums[r]: 
                _min.pop()
            _min.append((r, nums[r]))

            #now do the actual implemenation using sliding window
            while _max[0][1]-_min[0][1] > limit: 
                #move the left one pointer to the right 
                if _max[0][0] == left: 
                    _max.popleft()
                if _min[0][0] == left: 
                    _min.popleft()
                
                left += 1 

            ans = max(ans, r-left+1)
        return ans 