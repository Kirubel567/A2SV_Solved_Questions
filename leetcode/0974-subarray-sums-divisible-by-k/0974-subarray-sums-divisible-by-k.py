class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mapp = defaultdict(int)
        ans, _sum = 0, 0 
        mapp[0] = 1
        
        for num in nums: 
            _sum += num
            remainder = _sum%k 

            ans += mapp[remainder]
            mapp[remainder] +=1
        return ans 