class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n=1
        while(num-n*n)>0:
            n+=1
        return num-n*n==0 