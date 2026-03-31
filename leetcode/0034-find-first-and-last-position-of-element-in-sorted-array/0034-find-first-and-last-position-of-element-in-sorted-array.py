class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        ans = [-1, -1]
        while left <= right: 
            mid = (left+right)//2
            if nums[mid] == target: 
                left = right = mid

                while left >=0 and nums[left]==target: 
                    ans[0] = left
                    left-=1
                while right < len(nums) and nums[right] == target: 
                    ans[1] = right
                    right +=1 
                break 
            elif nums[mid] > target: 
                right = mid-1
            else:
                left = mid+1

        return ans 

