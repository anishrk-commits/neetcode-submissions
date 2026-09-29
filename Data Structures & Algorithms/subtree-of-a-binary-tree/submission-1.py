# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    same = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, subRoot):

            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None or root.val != subRoot.val:
                return False
            left = sameTree(root.left, subRoot.left)
            right = sameTree(root.right, subRoot.right)

            return left and right
        
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        
        check = sameTree(root, subRoot)
        if check:
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        


        
    

        