class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target>1:
            if target%2==0 and maxDoubles>0:
                target/=2
                maxDoubles-=1
                ans+=1
            elif maxDoubles==0:
                ans+=target-1
                break
            else:
                target-=1
                ans+=1
        return int(ans)