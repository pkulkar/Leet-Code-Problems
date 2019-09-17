class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans=list()
        for i in range(num+1):
            number=bin(i)
            ones=number.count("1")
            ans.append(ones)
            
        return ans