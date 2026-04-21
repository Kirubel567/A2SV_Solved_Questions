class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        for i in range(len(nums)): 
            if nums[i] == 0: 
                red += 1
            elif nums[i] == 1:
                white += 1
            else: 
                blue += 1
        
        white += red 
        blue += white
        
        for i in range(len(nums)): 
            if i < red: 
                nums[i] = 0
            elif i < white: 
                nums[i] =1
            else: 
                nums[i]=2
        
            

