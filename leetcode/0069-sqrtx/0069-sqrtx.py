class Solution:
    def mySqrt(self, x: int) -> int:
        left , right = 0, (x//2)+1
        while left <= right: 
            mid = (left+right)//2
            prd = mid*mid
            if prd == x: 
                return mid 
            elif prd > x: 
                right = mid -1
            else: 
                left = mid+1
        return right
