class Solution:
    def myPow(self, x: float, n: int) -> float:
        def _pow(x, n):
            if n == 0: 
                return 1
            
            half = _pow(x, n//2)
            if n%2==0:
                return half * half 
            else: 
                return x * half * half 
            
        if n<0: 
            x = 1/x
            n = abs(n)
        
        return _pow(x, n)


