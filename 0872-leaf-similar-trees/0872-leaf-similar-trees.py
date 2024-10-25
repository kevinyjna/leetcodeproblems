# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        result = []
        result2 = []

        def getLeaf(root, result):
            if root.left is None and root.right is None:
                result.append(root.val)
                print(result)
                return
            if root.left:
                getLeaf(root.left, result)
            if root.right:
                getLeaf(root.right, result)
            return
                
        getLeaf(root1, result)
        getLeaf(root2, result2)
        return  result == result2