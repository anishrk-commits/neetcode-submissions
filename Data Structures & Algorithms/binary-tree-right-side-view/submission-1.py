# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        queue = deque([root])

        results = []

        while queue:
            level = len(queue)
            for i in range(level - 1):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)
            
            curr = queue.popleft()
            results.append(curr.val)
            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
                
        return results
