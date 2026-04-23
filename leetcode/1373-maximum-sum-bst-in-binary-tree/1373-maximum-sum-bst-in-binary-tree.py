# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        _sum =0
        result = 0
        #max should be the least number float('-inf')
        #min should be the largest numbe float('inf')

        #[max, min, sum]
        #right side 
        #max
        #min -> this is what matters 
        #left_side
        #max -> this is what matters 
        #min 

        def dfs(node): 
            nonlocal result
            #base case, when null the sum would be 0
            if not node: 
                return [-float('inf'), float('inf'), 0]
            
            left_side=dfs(node.left)
            right_side=dfs(node.right)

            if node.val <= left_side[0] or node.val >= right_side[1]: 
                return [float('inf'), -float('inf'), 0]
            
            _sum = left_side[2]+node.val+right_side[2]
            result = max(result, _sum)

            return [max(left_side[0], node.val, right_side[0]), min(left_side[1], right_side[1], node.val),  _sum]
        
        dfs(root)
        return result