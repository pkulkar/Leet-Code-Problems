"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.height(root)
    
    def height(self, root):
        if not root:
            return 0
        left = 1 + self.height(root.left)
        right = 1 + self.height(root.right)
        return max(left, right)

"""
Time Complexity: O(n)
Space Complexity: O(h) where h is the height of tree
"""