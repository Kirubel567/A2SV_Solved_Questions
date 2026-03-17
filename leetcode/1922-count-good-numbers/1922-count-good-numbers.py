class Solution:
    def countGoodNumbers(self, n: int) -> int:
        #even numbers 0, 2, 4, 6, 8
        #prime numbers 2,3,5,7,

        #calculation if evevn half*half
        #calculation if odd half*half * 5

        if n %2==0: 
            return (pow(5,(n//2), (1000000000+7)) * pow(4,(n//2), (1000000000+7)))%(1000000000+ 7)
        else: 
            return (pow(5,((n-1)//2), (1000000000+7))* pow(4,((n-1)//2), (1000000000+7)) *5)%(1000000000+7)

