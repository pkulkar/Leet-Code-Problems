"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        nums.sort()
        memory = [0] * (len(nums))
        
        for i, num in enumerate(nums):
            maxSize = 0
            for k in range(0, i):
                if nums[i] % nums[k] == 0:
                    maxSize = max(maxSize, memory[k])

            maxSize += 1
            memory[i] = maxSize
        
        maxSize, Index = max([(v, i) for i, v in enumerate(memory)])
        result = []

        current_Size, current_Tail = maxSize, nums[Index]
        for i in range(Index, -1, -1):
            if current_Size == memory[i] and current_Tail % nums[i] == 0:
                result.append(nums[i])
                current_Size -= 1
                current_Tail = nums[i]
        
        return result[::-1]

"""
Time Complexity: O(N^2)
Space Complexity: O(N)
"""