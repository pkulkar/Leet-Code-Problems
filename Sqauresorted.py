class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        square=list()
        s=0
        for a in A:
            s=a*a
            square.append(s)
        square.sort()
        return square
        