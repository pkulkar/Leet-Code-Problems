"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.
"""

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #Edge Check
        if len(costs) < 1:
            return 0
        
        #Start from row 1 as we have no choice for the 0th row
        for i in range(1, len(costs)):
            for j in range(len(costs[0])):
            	
            	#Elimniate current column choice from prev row as we can't use same colors adjecently
                prev_row = costs[i-1][:j] + costs[i-1][j+1:] 
                costs[i][j] += min(prev_row)

        #Return min from last row as that is the aggregated min cost
        return min(costs[len(costs)-1]) 
"""
Time Complexity: O(m+n) where m is number of rows and n is number of columns
Space Complexity: O(1) as alteration is being done inside the matrix
"""