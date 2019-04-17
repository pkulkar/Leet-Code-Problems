class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        A=f'{x:032b}'
        B=f'{y:032b}'
        count=0
        for i in range(32):
            if A[i] != B[i]:
                count+=1
        return count