class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        _max = deque()
        ans = [] 
        for r in range(len(nums)): 
            while _max and _max[-1]<nums[r]:
                _max.pop()
            _max.append(nums[r])

            if r >= k and nums[r-k] == _max[0]: 
                _max.popleft()
            if r >= k-1: 
                ans.append(_max[0])
        return ans 