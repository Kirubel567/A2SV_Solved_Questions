class Solution:
    def power(self, x: int, n: int) -> float:
        if n == 0: 
            return 1
        half = self.power(x, n//2)
        if n %2==0: 
            return (half*half)%(10**9 + 7)
    
        return (x*half*half)%(10**9 + 7)

    def countGoodNumbers(self, n: int) -> int:
        prime = n//2
        even = n//2 if n%2==0 else (n+1)//2 
    
        return (self.power(5, even) *self.power(4,prime))%(1000000000+7)
