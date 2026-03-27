# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #do dfs on the root 
        #if one node is the same as the subRoot then compare each and every nodes comeing after them 
        def dfs(node1, node2):            
                if not node1 and not node2: 
                    return True 
                if not node1 or not node2: 
                    return False
                if node1.val != node2.val: 
                    return False
                
                return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
        if not root: 
            return False
            
        return dfs(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            



