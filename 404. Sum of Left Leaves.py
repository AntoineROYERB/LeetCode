# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(node, isLeft):
            if not node: return 0
            if not node.left and not node.right:
                if isLeft: return node.val
                else: 0
            sum_left = dfs(node.left, True)
            sum_right = dfs(node.right, False)
            return sum_left + sum_right
        return dfs(root, False)