"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \  / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""
#Solution 1: Recursive
"""
Time Complexity: O(n)
Space Complexity: O(d) Depth of the tree
"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

#Solution 1: Iterative
"""
Time Complexity: O(n)
Space Complexity: O(n) 
"""
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
