class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        max_area = -float('inf')

        while start < end: 
            max_area = max(max_area, min(height[start], height[end]) * (end-start))
            if height[start] <= height[end]: 
                start += 1
            else: 
                end -= 1
        return max_area 