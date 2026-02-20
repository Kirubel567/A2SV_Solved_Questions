class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        mapp = Counter(nums)
        for key, value in mapp.items(): 
            if value > len(nums)//3: 
                ans.append(key)
        return ans 
        