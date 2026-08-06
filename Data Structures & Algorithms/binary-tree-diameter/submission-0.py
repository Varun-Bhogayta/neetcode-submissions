# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0  # Global variable to store max diameter

        def dfs(curr):
            if not curr:
                return -1  # Height of an empty node/tree in terms of edges

            left = dfs(curr.left)
            right = dfs(curr.right)

            # Diameter passing through curr node is the sum of edge counts of both subtrees
            self.res = max(self.res, 2 + left + right)

            # Return height of curr node to its parent
            return 1 + max(left, right)

        dfs(root)
        return self.res