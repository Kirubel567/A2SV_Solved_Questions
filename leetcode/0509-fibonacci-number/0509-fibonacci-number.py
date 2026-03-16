class Solution:
    def fib(self, n: int) -> int:
        #iterative way 
        #a, b 
        a = 0
        b = 1
        if n == 0: 
            return 0
        for i in range(n-1): 
            c = a + b 
            a = b 
            b = c
        return b
