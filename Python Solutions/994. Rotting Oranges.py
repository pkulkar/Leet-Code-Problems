"""
994. Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.

"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited_set = set()
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    queue.append((i,j, 0))
        minutes = 0
        while queue:
            size = len(queue)
            for i in range(size):
                x, y, minutes = queue.popleft()
                for dx, dy in directions:
                    if self.is_valid(x+dx,y+dy, grid) and (x+dx,y+dy) not in visited_set:
                        visited_set.add((x+dx, y+dy))
                        grid[x+dx][y+dy] = 2
                        queue.append((x+dx, y+dy, minutes + 1))

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    return -1 

        return minutes
    
    def is_valid(self, row, col, grid):
        if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == 1:
            return True
        return False

"""
Time complexity: O(m + n) m and n are number of rows and cols repectively
Space Complexity: O(m + n)
"""
