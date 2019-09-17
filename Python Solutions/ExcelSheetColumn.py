class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        col=0
        for i in range(0,len(s)):
            col=col+(pow(26,len(s)-i-1)*(ord(s[i])-64))
        return col
            