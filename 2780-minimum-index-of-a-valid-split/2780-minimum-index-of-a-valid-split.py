class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        mapp = Counter(nums)
        f, x = 0, 0
        Max = -float('inf')
        for key, value in mapp.items(): 
            if mapp[key] > Max: 
                f = mapp[key]
                Max = f
                x = key
        f1 = 0
        for i in range(len(nums)-1): 
            if nums[i] == x: 
                f1 += 1
            f2 = f-f1
            if f1 > (i+1)//2 and f2 > (len(nums)-i-1)//2:
                return i
        return -1

            
