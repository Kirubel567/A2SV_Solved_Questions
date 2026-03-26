class Solution:
    def lastRemaining(self, n: int) -> int:
        def recur(n): 
            if n ==1: 
                return 1
            
            return 2*(n//2+1-recur(n//2))

        return recur(n)