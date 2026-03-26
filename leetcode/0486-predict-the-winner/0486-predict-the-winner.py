class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def recur(l, r): 
            if l>=r: 
                return nums[l]
            
            return max(nums[l]-recur(l+1, r), nums[r]-recur(l, r-1))
            
        return recur(0, len(nums)-1) >=0


                

            


        