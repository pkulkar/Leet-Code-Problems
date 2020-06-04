"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i * i for i in range(1, int(n**0.5)+1)]
        level = 0
        queue = {n}
        while queue:
            level += 1
            next_queue = set()
            for remainder in queue:
                for square_num in square_nums:    
                    if remainder == square_num:
                        return level  # find the node!
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue
        return level

"""
Time Complexity: O(n ^ h/2) :: we construct n-ary tree an traverse in BFS manner h is the height
Space Complexity: O((n ^ 1/2) ^ h)
"""