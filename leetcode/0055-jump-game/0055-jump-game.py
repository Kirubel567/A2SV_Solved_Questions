class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, next_jmp = len(nums)-2, len(nums)-1
        while i >-1: 
            if i + nums[i] >= next_jmp: 
                next_jmp = i 
            i -= 1
        return True if next_jmp==0 else False