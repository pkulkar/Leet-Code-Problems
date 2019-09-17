class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        number=str()
        for i in range(len(A)):
            number+=str(A[i])
        num=int(number)
        ans=num+K
        answer=str(ans)
        l=list()
        for i in range(len(answer)):
            l.append(answer[i])
        return l