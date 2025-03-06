# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        paths = []
        def getPaths(par, path=""):
            path += str(par.val)
            if par.left:
                getPaths(par.left, path+"->")
            if par.right:
                getPaths(par.right, path+"->")
            if not par.left and not par.right:
                paths.append(path)
        getPaths(root)
        return paths