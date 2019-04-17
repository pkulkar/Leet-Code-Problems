class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even=list()
        odd=list()
        for a in A:
            if a % 2==0:
                even.append(a)
            else:
                odd.append(a)
        answer=list()
        answer=even+odd
        return answer