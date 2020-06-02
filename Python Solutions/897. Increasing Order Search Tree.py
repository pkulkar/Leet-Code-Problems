"""
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
 

Constraints:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
"""

"""
Time Complexity: O(n)
Space Complexity: O(h) where h is height of the tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = list()
        self.inorder(root, nodes)
        preNode = TreeNode(-1)
        root = preNode
        for node in nodes:
            if node:
                preNode.right = TreeNode(node.val)
                preNode = preNode.right
        return root.right

    def inorder(self, root, nodes):
        if not root:
            return
        nodes.append(self.inorder(root.left, nodes))
        nodes.append(root)
        nodes.append(self.inorder(root.right, nodes))