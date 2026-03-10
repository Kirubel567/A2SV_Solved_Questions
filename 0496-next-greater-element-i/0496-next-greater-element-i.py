class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp = defaultdict(lambda : -1)
        stk = []
        for num in nums2: 
            while stk and stk[-1] < num: 
                mapp[stk.pop()] = num 
            stk.append(num)
        return [mapp[nums1[i]] for i in range(len(nums1))] 