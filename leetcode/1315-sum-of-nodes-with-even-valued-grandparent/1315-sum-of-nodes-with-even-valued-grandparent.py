# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        _sum = 0
        def dfs(node, parent, grandpa): 
            nonlocal _sum
            if not node: 
                return 
            if grandpa and grandpa.val%2==0: 
                _sum += node.val
            
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)
        dfs(root, None, None)
        return _sum