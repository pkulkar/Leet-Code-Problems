import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=re.sub('\W+','', s)
        if s=="":
            return True
        s=s.lower()
        l=len(s)
        for i in range(len(s)//2+1):
            if s[i]!=s[l-1-i]:
                return False
        return True