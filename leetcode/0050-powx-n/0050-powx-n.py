class Solution:
    def power(self, x: float, n: int)->float: 
        if n == 0: 
            return 1
    
        half = self.power(x, n//2)
        if n%2==0:
            return half*half
        return x*half*half

    def myPow(self, x: float, n: int) -> float:
        #base case
        #recurrence relation 
        #state changes 
        if n <0: 
            n = abs(n)
            x =1/x
        return self.power(x, n)