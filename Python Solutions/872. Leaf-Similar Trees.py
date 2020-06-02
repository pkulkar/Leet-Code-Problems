"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
			
			3
		   / \
		  5   1
		 / \  | \
		6   2 9  8
		   / \
		  7   4

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Constraints:

Both of the given trees will have between 1 and 200 nodes.
Both of the given trees will have values between 0 and 200
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.leaf_sequence(root1) == self.leaf_sequence(root2)
          
    def leaf_sequence(self, root):
        if not root:
            return []
        leaf_list = []
        stack = [root]
        while stack:
            current_level, size = [], len(stack)
            for _ in range(size):
                node = stack.pop()
                if not node.right and not node.left:
                    leaf_list.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return leaf_list

 """
 Time complexity: O(n)
 Space complexity: O(n)
 """
