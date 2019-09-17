class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                return True
            else:
                d[nums[i]]=1
        return False
        