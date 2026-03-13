class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        _max = deque()
        ans = []
        for i in range(k): 
            while _max and _max[-1]<nums[i]: 
                _max.pop()
            _max.append(nums[i])
        ans.append(_max[0])
        
        for r in range(k, len(nums)): 
            while _max and _max[-1]<nums[r]:
                _max.pop()
            _max.append(nums[r])

            if nums[r-k] == _max[0]: 
                _max.popleft()

            ans.append(_max[0])
        return ans 