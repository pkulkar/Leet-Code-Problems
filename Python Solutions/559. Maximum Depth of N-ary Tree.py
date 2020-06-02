"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:

			1
		  / | \
		 3  2  4
	    / \
	   5   6

Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Example 2:

		   1
		/ |   |   \
	   2  3   4    5
		 / \  |   / \
		6   7 8  9  10
			| |  |
		  11  12 13
			|
			14
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5	
 

Constraints:

The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [0, 10^4].
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        max_height = 0
        while queue:
            current_level, size = [], len(queue)
            for _ in range(size):
                node, height = queue.popleft()
                max_height = max(max_height, height)
                for i in range(len(node.children)):
                    if node.children[i]:
                        queue.append((node.children[i], height + 1))
        return max_height
 
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""