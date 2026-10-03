# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    lca = -101
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search_p(root, p):
            if not root:
                return False
            
            if root == p:
                return True
            
            left = search_p(root.left, p)
            right = search_p(root.right,p)

            return left or right
        def search_q(root, q):
            if not root:
                return False
            
            if root == q:
                return True
            
            left = search_q(root.left, q)
            right = search_q(root.right,q)

            return left or right
        
        if not root:
            return self.lca
        
        if search_p(root, p) and search_q(root, q):
            self.lca = root
        
        self.lowestCommonAncestor(root.left, p, q)
        self.lowestCommonAncestor(root.right, p, q)

        return self.lca

        




        
