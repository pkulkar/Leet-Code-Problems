"""
Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.

If there is no common element, return -1.

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
 

Constraints:

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in increasing order.
"""

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        comparision_row = mat[0]
        minimum_element = float("inf")
        for i in range(len(comparision_row)):
            element = comparision_row[i]
            count = 1
            for j in range(1, len(mat)):
                count += self.binary_search(mat[j], element)
            if count == len(mat):
                minimum_element = min(minimum_element, element)
        if minimum_element == float(inf):
            return -1
        return minimum_element
    
    def binary_search(self, arr, element):
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if arr[mid] == element:
                return 1
            if arr[mid] > element:
                right = mid - 1
            if arr[mid] < element:
                left = mid + 1
        if arr[left] == element: return 1
        if arr[right] == element: return 1
        return 0
                
"""
Time Complexity: O(mnlgm)
Space Complexity: O(m)
"""
