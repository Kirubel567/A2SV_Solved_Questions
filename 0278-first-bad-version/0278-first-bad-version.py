# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        bad = n 
        while low <= high: 
            middle = (low + high)//2
            if isBadVersion(middle):
                bad = middle 
                high = middle - 1
            else: 
                low = middle + 1
        
        return bad
            
