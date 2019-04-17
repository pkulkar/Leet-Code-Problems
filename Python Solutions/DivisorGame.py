class Solution:    
    def divisorGame(self, N: int) -> bool:
        count=1
        while N>1:
            for x in range(1,N,1):
                if N % x==0:
                    break
            count+=1
            N-=x
        if count % 2==0:
            return True
        else:
            return False