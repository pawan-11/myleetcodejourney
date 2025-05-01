# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def help(root):
            if not root:
                return float('-inf'),float('-inf') 
            mxpath_l, mxleaf_l = help(root.left)
            mxpath_r, mxleaf_r = help(root.right)
            return max(mxpath_l, mxpath_r, mxleaf_l, mxleaf_l+root.val, mxleaf_l+root.val   +mxleaf_r, mxleaf_r+root.val, root.val), max(root.val+mxleaf_l, root.val+mxleaf_r, root.val)
        
        return help(root)[0]