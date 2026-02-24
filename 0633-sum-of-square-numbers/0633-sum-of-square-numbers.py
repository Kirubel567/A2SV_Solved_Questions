class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        #this is a math question 
        #iterage up until sqrt(c)

        start, end = 0, int(c**(1/2))
        while start <= end: 
            Sum = start**2 + end**2
            if Sum > c: 
                end -= 1
            elif Sum < c: 
                start += 1
            else: 
                return True 
        return False
