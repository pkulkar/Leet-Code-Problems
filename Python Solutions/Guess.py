# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(1)==0:
            return 1
        if guess(n)==0:
            return n
        g=n//2
        c=guess(g)
        while c!=0:
            if c<0:
                n=g
                g=g//2
            else:
                temp=g
                g=(temp+n)//2
            c=guess(g)
        return g
