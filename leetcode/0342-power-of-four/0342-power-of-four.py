class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 4 or n == 1: 
            return True 
        elif n < 4 and n !=1: 
            return False
        
        n = n ** 1/4
        return self.isPowerOfFour(n)
    
       