class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        size=len(A)
        N=int(size/2)
        for a in A:
            p=A.count(a)
            if p==N:
                return a